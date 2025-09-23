"""
Sistema de Webhook para receber dados do Tally
Processa formulários automaticamente e integra com IA
"""

from flask import Flask, request, jsonify
import json
import pandas as pd
from datetime import datetime
import os
import sys

# Adicionar src ao path para imports
sys.path.append(os.path.dirname(__file__))

from services.marketing_analysis_engine import MarketingAnalysisEngine
from services.proposal_generator import ProposalGenerator

app = Flask(__name__)

# Configurações
WEBHOOK_SECRET = "tally_webhook_secret_2024"  # Trocar por token seguro
DATA_DIR = "data/submissions"

# Criar diretório se não existir
os.makedirs(DATA_DIR, exist_ok=True)

def processar_dados_tally(data):
    """Converte dados do Tally para formato do sistema IA"""
    
    # Mapeamento dos campos do Tally para sistema interno
    dados_processados = {
        'nome_empresa': data.get('nome_empresa', ''),
        'produto_servico': data.get('produto_servico', ''),
        'descricao_empresa': data.get('descricao_empresa', ''),
        'fundacao': data.get('fundacao', ''),
        'endereco': data.get('endereco', ''),
        'alcance_clientes': data.get('alcance_clientes', ''),
        'objetivos_12m': data.get('objetivos_12m', ''),
        
        # Cliente e jornada
        'cliente_ideal': data.get('cliente_ideal', ''),
        'como_descobrem': data.get('como_descobrem', []),
        'o_que_valorizam': data.get('o_que_valorizam', ''),
        'principal_dor': data.get('principal_dor', ''),
        'satisfacao_atendimento': int(data.get('satisfacao_atendimento', 3)),
        'probabilidade_indicacao': int(data.get('probabilidade_indicacao', 5)),
        
        # Concorrência
        'principais_concorrentes': data.get('principais_concorrentes', ''),
        'diferencial_unico': data.get('diferencial_unico', ''),
        'marketing_concorrentes': data.get('marketing_concorrentes', ''),
        
        # Operações
        'canais_vendas': data.get('canais_vendas', []),
        'canal_mais_receita': data.get('canal_mais_receita', ''),
        'marketing_atual': data.get('marketing_atual', ''),
        'meta_aumento_vendas': data.get('meta_aumento_vendas', ''),
        
        # Online
        'presenca_online': data.get('presenca_online', ''),
        'ferramenta_crm': data.get('ferramenta_crm', ''),
        'canal_online_principal': data.get('canal_online_principal', ''),
        
        # Extras
        'informacoes_adicionais': data.get('informacoes_adicionais', ''),
        
        # Metadados
        'data_submissao': datetime.now().isoformat(),
        'submission_id': data.get('submission_id', ''),
        'form_id': data.get('form_id', '')
    }
    
    return dados_processados

def executar_analise_automatica(dados_cliente):
    """Executa análise IA automaticamente"""
    
    try:
        # Inicializar motor de análise
        engine = MarketingAnalysisEngine()
        
        # Executar análise
        analise = engine.analisar_cliente_completo(dados_cliente)
        
        # Gerar proposta
        generator = ProposalGenerator()
        proposta = generator.gerar_proposta_completa(dados_cliente, analise)
        
        # Salvar resultados
        resultado = {
            'cliente': dados_cliente,
            'analise': analise.__dict__ if hasattr(analise, '__dict__') else analise,
            'proposta': proposta.__dict__ if hasattr(proposta, '__dict__') else proposta,
            'processado_em': datetime.now().isoformat()
        }
        
        # Salvar em arquivo
        filename = f"{DATA_DIR}/analise_{dados_cliente['submission_id']}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
        
        return resultado
        
    except Exception as e:
        print(f"Erro na análise automática: {e}")
        return None

@app.route('/webhook/tally', methods=['POST'])
def webhook_tally():
    """Endpoint para receber dados do Tally"""
    
    try:
        # Verificar content type
        if request.content_type != 'application/json':
            return jsonify({'error': 'Content-Type deve ser application/json'}), 400
        
        # Receber dados
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON inválidos'}), 400
        
        # Verificar token de segurança (opcional)
        auth_header = request.headers.get('Authorization', '')
        if WEBHOOK_SECRET not in auth_header:
            print("Warning: Webhook sem autenticação adequada")
        
        # Processar dados do Tally
        dados_processados = processar_dados_tally(data.get('data', {}))
        
        # Log da submissão
        print(f"📋 Nova submissão recebida: {dados_processados['nome_empresa']}")
        print(f"🕐 Timestamp: {dados_processados['data_submissao']}")
        
        # Executar análise automática
        resultado_analise = executar_analise_automatica(dados_processados)
        
        if resultado_analise:
            print(f"✅ Análise concluída para: {dados_processados['nome_empresa']}")
            
            # Resposta de sucesso
            response = {
                'status': 'success',
                'message': 'Análise processada com sucesso',
                'submission_id': dados_processados['submission_id'],
                'empresa': dados_processados['nome_empresa'],
                'processado_em': dados_processados['data_submissao']
            }
            
            return jsonify(response), 200
        else:
            print(f"❌ Erro no processamento para: {dados_processados['nome_empresa']}")
            
            # Salvar dados mesmo com erro na análise
            filename = f"{DATA_DIR}/dados_brutos_{dados_processados['submission_id']}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(dados_processados, f, ensure_ascii=False, indent=2)
            
            return jsonify({
                'status': 'partial_success', 
                'message': 'Dados salvos, análise pendente'
            }), 202
            
    except Exception as e:
        print(f"💥 Erro no webhook: {e}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@app.route('/webhook/test', methods=['POST', 'GET'])
def test_webhook():
    """Endpoint para testar webhook"""
    
    if request.method == 'GET':
        return jsonify({
            'status': 'webhook_active',
            'timestamp': datetime.now().isoformat(),
            'message': 'Webhook funcionando corretamente'
        })
    
    # POST - simular dados do Tally
    dados_teste = {
        "form_id": "test_form",
        "submission_id": f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "submitted_at": datetime.now().isoformat(),
        "data": {
            "nome_empresa": "Empresa Teste",
            "produto_servico": "Consultoria",
            "descricao_empresa": "Empresa de teste para validação",
            "fundacao": "2020",
            "endereco": "São Paulo, SP",
            "alcance_clientes": "Regional",
            "objetivos_12m": "Testar o sistema de análise automática",
            "cliente_ideal": "Empresas pequenas e médias",
            "como_descobrem": ["Indicação de amigos", "Google"],
            "o_que_valorizam": "Qualidade e preço justo",
            "principal_dor": "Falta de visibilidade online",
            "satisfacao_atendimento": 4,
            "probabilidade_indicacao": 8,
            "principais_concorrentes": "Concorrente A, B e C",
            "diferencial_unico": "Atendimento personalizado",
            "marketing_concorrentes": "Redes sociais e Google Ads",
            "canais_vendas": ["Loja física", "WhatsApp"],
            "canal_mais_receita": "Loja física",
            "marketing_atual": "Básico nas redes sociais",
            "meta_aumento_vendas": "30% no próximo ano"
        }
    }
    
    # Processar como webhook normal
    return webhook_tally()

@app.route('/submissions', methods=['GET'])
def listar_submissoes():
    """Lista todas as submissões processadas"""
    
    try:
        arquivos = os.listdir(DATA_DIR)
        submissoes = []
        
        for arquivo in arquivos:
            if arquivo.endswith('.json'):
                with open(f"{DATA_DIR}/{arquivo}", 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    
                    submissoes.append({
                        'arquivo': arquivo,
                        'empresa': dados.get('cliente', {}).get('nome_empresa', 'N/A'),
                        'data': dados.get('processado_em', 'N/A'),
                        'status': 'processado' if 'analise' in dados else 'pendente'
                    })
        
        return jsonify({
            'total': len(submissoes),
            'submissoes': sorted(submissoes, key=lambda x: x['data'], reverse=True)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submission/<submission_id>', methods=['GET'])
def obter_submissao(submission_id):
    """Obtém dados de uma submissão específica"""
    
    try:
        filename = f"{DATA_DIR}/analise_{submission_id}.json"
        
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            return jsonify(dados)
        else:
            return jsonify({'error': 'Submissão não encontrada'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Iniciando servidor webhook...")
    print(f"📍 Endpoint principal: http://localhost:5000/webhook/tally")
    print(f"🧪 Endpoint teste: http://localhost:5000/webhook/test")
    print(f"📋 Listar submissões: http://localhost:5000/submissions")
    
    app.run(debug=True, host='0.0.0.0', port=5000)