"""
Agente de Marketing IA - Assistente de Consultor
Interface para análise de clientes e geração de propostas de marketing
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from pathlib import Path
import sys
import os

# Adicionar src ao path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from services.marketing_analysis_engine import MarketingAnalysisEngine

# Configuração da página
st.set_page_config(
    page_title="🤖 Agente Marketing IA - Assistente de Consultor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Função principal da aplicação"""
    
    # Header principal
    st.title("🤖 Agente de Marketing IA")
    st.markdown("### 🎯 **Assistente Inteligente para Consultores de Marketing**")
    
    # Sidebar com navegação
    with st.sidebar:
        st.header("🎯 Assistente de Consultor")
        
        opcao = st.selectbox(
            "📋 Escolha sua atividade:",
            [
                "🏠 Visão Geral",
                "📝 Novo Cliente",
                "📊 Analisar Cliente", 
                "📋 Gerar Proposta",
                "👥 Clientes Salvos",
                "📚 Base de Conhecimento"
            ]
        )
    
    # Conteúdo principal baseado na seleção
    if opcao == "🏠 Visão Geral":
        show_overview()
    elif opcao == "📝 Novo Cliente":
        collect_client_data()
    elif opcao == "📊 Analisar Cliente":
        analyze_client()
    elif opcao == "📋 Gerar Proposta":
        generate_proposal()
    elif opcao == "👥 Clientes Salvos":
        show_saved_clients()
    elif opcao == "📚 Base de Conhecimento":
        show_knowledge_base()

def show_overview():
    """Tela de visão geral do assistente"""
    
    st.markdown("## 🏠 Visão Geral do Assistente")
    
    # Cards informativos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="👥 Clientes Analisados",
            value="15",
            delta="3 este mês"
        )
    
    with col2:
        st.metric(
            label="📋 Propostas Geradas", 
            value="23",
            delta="7 este mês"
        )
    
    with col3:
        st.metric(
            label="💰 ROI Médio Projetado",
            value="180%",
            delta="15% vs mês anterior"
        )
    
    st.markdown("---")
    
    # Fluxo de trabalho
    st.markdown("## 🔄 **Fluxo de Trabalho do Assistente**")
    
    flow_steps = [
        ("📝", "Coleta de Dados", "Insira informações do cliente: setor, desafios, objetivos"),
        ("🤖", "Análise IA", "IA processa dados e identifica oportunidades"),
        ("💡", "Insights", "Geração automática de insights e recomendações"),
        ("📋", "Proposta", "Criação de plano de marketing personalizado"),
        ("🎯", "Apresentação", "Material profissional para apresentar ao cliente")
    ]
    
    cols = st.columns(5)
    for i, (icon, title, desc) in enumerate(flow_steps):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; border: 2px solid #f0f2f6; border-radius: 10px; margin: 10px;">
                <h2>{icon}</h2>
                <h4>{title}</h4>
                <p style="font-size: 12px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Benefícios
    st.markdown("## ✨ **Benefícios para o Consultor**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🚀 **Eficiência**
        - ⏱️ Economiza 80% do tempo de análise
        - 🔄 Processo padronizado e escalável
        - 📊 Análise baseada em dados reais
        - 🎯 Foco no que realmente importa
        """)
    
    with col2:
        st.markdown("""
        ### 💼 **Profissionalismo**
        - 📋 Propostas com aparência profissional
        - 🎯 Precisão nas recomendações
        - 📈 ROI projetado com base em dados
        - 🏆 Credibilidade aumentada
        """)

def collect_client_data():
    """Interface para coletar dados do cliente"""
    
    st.markdown("## 📝 **Novo Cliente - Coleta de Dados**")
    
    with st.form("client_data_form"):
        # Informações básicas
        st.markdown("### 🏢 **Informações Básicas**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nome_cliente = st.text_input("👤 Nome do Cliente/Empresa")
            setor = st.selectbox(
                "🏭 Setor de Atuação",
                [
                    "Selecione...",
                    "E-commerce/Varejo Online",
                    "Representação Comercial", 
                    "Consultoria/Serviços",
                    "Indústria/Manufatura",
                    "Tecnologia/Software",
                    "Saúde/Medicina",
                    "Educação/Treinamento",
                    "Imobiliário",
                    "Alimentação/Restaurantes",
                    "Outros"
                ]
            )
            
        with col2:
            porte_empresa = st.selectbox(
                "📏 Porte da Empresa",
                ["MEI", "Microempresa", "Pequena", "Média", "Grande"]
            )
            orcamento = st.selectbox(
                "💰 Orçamento Mensal para Marketing",
                [
                    "Até R$ 5.000",
                    "R$ 5.001 - R$ 15.000", 
                    "R$ 15.001 - R$ 50.000",
                    "R$ 50.001 - R$ 100.000",
                    "Acima de R$ 100.000"
                ]
            )
        
        # Situação atual
        st.markdown("### 📊 **Situação Atual**")
        
        desafios = st.multiselect(
            "🎯 Principais Desafios",
            [
                "Baixa geração de leads",
                "Conversão baixa",
                "Ciclo de vendas muito longo",
                "Falta de conhecimento da concorrência",
                "Problemas de marca/posicionamento",
                "Canais de marketing ineficientes",
                "Falta de dados/métricas",
                "Time de marketing inexperiente",
                "Orçamento limitado",
                "Dificuldade em medir ROI"
            ]
        )
        
        canais_atuais = st.multiselect(
            "📱 Canais de Marketing Atuais",
            [
                "Google Ads",
                "Facebook/Instagram Ads",
                "LinkedIn Ads", 
                "Email Marketing",
                "SEO/Blog",
                "Indicações/Networking",
                "Vendas diretas",
                "Marketplaces",
                "Eventos/Feiras",
                "Influenciadores",
                "Assessoria de Imprensa"
            ]
        )
        
        # Objetivos
        st.markdown("### 🎯 **Objetivos e Metas**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            objetivo_principal = st.selectbox(
                "🎯 Objetivo Principal",
                [
                    "Aumentar vendas",
                    "Gerar mais leads",
                    "Melhorar conversão",
                    "Reduzir custo de aquisição",
                    "Aumentar reconhecimento da marca",
                    "Expandir para novos mercados",
                    "Fidelizar clientes existentes",
                    "Lançar novo produto/serviço"
                ]
            )
            
        with col2:
            prazo = st.selectbox(
                "⏰ Prazo para Resultados",
                ["1-3 meses", "3-6 meses", "6-12 meses", "12+ meses"]
            )
        
        meta_crescimento = st.slider(
            "📈 Meta de Crescimento (%)",
            min_value=10,
            max_value=500,
            value=50,
            step=10
        )
        
        # Informações adicionais
        observacoes = st.text_area(
            "📝 Observações Adicionais",
            placeholder="Informações importantes sobre o cliente, histórico, particularidades do setor, etc."
        )
        
        # Botão de submissão
        submitted = st.form_submit_button("💾 Salvar Cliente e Continuar para Análise")
        
        if submitted:
            if nome_cliente and setor != "Selecione...":
                # Salvar dados do cliente
                client_data = {
                    "nome": nome_cliente,
                    "setor": setor,
                    "porte": porte_empresa,
                    "orcamento": orcamento,
                    "desafios": desafios,
                    "canais_atuais": canais_atuais,
                    "objetivo_principal": objetivo_principal,
                    "prazo": prazo,
                    "meta_crescimento": meta_crescimento,
                    "observacoes": observacoes,
                    "data_criacao": datetime.now().isoformat()
                }
                
                # Salvar em session state
                st.session_state['current_client'] = client_data
                
                st.success(f"✅ Dados do cliente '{nome_cliente}' salvos com sucesso!")
                st.info("🎯 Agora você pode ir para 'Analisar Cliente' para gerar insights automáticos.")
                
            else:
                st.error("❌ Por favor, preencha pelo menos o nome e setor do cliente.")

def analyze_client():
    """Interface para análise do cliente"""
    
    st.markdown("## 📊 **Análise Inteligente do Cliente**")
    
    if 'current_client' not in st.session_state:
        st.warning("⚠️ Nenhum cliente carregado. Vá para 'Novo Cliente' primeiro.")
        return
    
    client = st.session_state['current_client']
    
    # Mostrar dados do cliente
    with st.expander("👤 Dados do Cliente", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Nome:** {client['nome']}")
            st.write(f"**Setor:** {client['setor']}")
            st.write(f"**Porte:** {client['porte']}")
        with col2:
            st.write(f"**Orçamento:** {client['orcamento']}")
            st.write(f"**Objetivo:** {client['objetivo_principal']}")
            st.write(f"**Prazo:** {client['prazo']}")
    
    if st.button("🤖 Executar Análise IA"):
        # Análise usando o motor de IA
        with st.spinner("🔄 IA analisando perfil do cliente..."):
            
            # Inicializar motor de análise
            engine = MarketingAnalysisEngine()
            
            # Executar análise completa
            analysis_result = engine.analyze_client(client)
            
            # Salvar resultado da análise
            st.session_state['current_analysis'] = analysis_result
        
        # Mostrar resultados
        st.markdown("## 💡 **Insights Gerados pela IA**")
        
        # Score geral
        scores = analysis_result['scores']
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("🎯 Score de Potencial", f"{scores['potential_score']:.1f}/10", "Alto Potencial")
        with col2:
            st.metric("📊 Complexidade", scores['complexity_score'], "Gerenciável")
        with col3:
            st.metric("💰 ROI Projetado", scores['roi_projection'], scores['time_to_results'])
        with col4:
            st.metric("🚀 Prioridade", scores['priority'], f"✅ {scores['success_probability']}")
        
        # Insights detalhados
        show_detailed_analysis(analysis_result)
        
        st.success("✅ Análise concluída! Agora você pode gerar a proposta.")

def show_detailed_analysis(analysis_result):
    """Mostrar análise detalhada"""
    
    insights = analysis_result['insights']
    recommendations = analysis_result['recommendations']
    risks = analysis_result['risk_assessment']
    metrics = analysis_result['success_metrics']
    
    # Insights por categoria
    st.markdown("### 🎯 **Insights Estratégicos**")
    
    # Separar insights por categoria
    insight_categories = {}
    for insight in insights:
        if insight.categoria not in insight_categories:
            insight_categories[insight.categoria] = []
        insight_categories[insight.categoria].append(insight)
    
    # Mostrar insights em tabs
    if insight_categories:
        tab_names = list(insight_categories.keys())
        tabs = st.tabs(tab_names)
        
        for i, (category, category_insights) in enumerate(insight_categories.items()):
            with tabs[i]:
                for insight in category_insights[:3]:  # Limitar a 3 por categoria
                    with st.expander(f"🎯 {insight.titulo}", expanded=False):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.write(f"**Descrição:** {insight.descricao}")
                            st.write(f"**Implementação:** {insight.prazo_implementacao}")
                        
                        with col2:
                            st.metric("🎯 Prioridade", insight.prioridade)
                            st.metric("📈 Impacto", insight.impacto_estimado)
                            st.metric("⚙️ Complexidade", insight.complexidade)
    
    # Recomendações prioritárias
    st.markdown("### 💡 **Recomendações Prioritárias**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### ✅ **Ações Imediatas**")
        for i, rec in enumerate(recommendations[:3], 1):
            st.success(f"{i}. {rec}")
    
    with col2:
        st.markdown("#### ⚠️ **Riscos a Monitorar**")
        for risk in risks[:3]:
            st.warning(f"**{risk['risk']}**: {risk['description']}")
    
    # Métricas de sucesso
    st.markdown("### 📊 **Métricas de Sucesso**")
    
    if metrics:
        metrics_df = pd.DataFrame(metrics)
        st.dataframe(metrics_df, use_container_width=True)
    
    # Gráfico de prioridades
    if insights:
        st.markdown("### 📈 **Distribuição de Prioridades**")
        
        priority_counts = {}
        for insight in insights:
            priority_counts[insight.prioridade] = priority_counts.get(insight.prioridade, 0) + 1
        
        if priority_counts:
            fig = px.pie(
                values=list(priority_counts.values()),
                names=list(priority_counts.keys()),
                title="Distribuição de Insights por Prioridade",
                color_discrete_map={
                    "Alta": "#ff6b6b",
                    "Média": "#ffd93d", 
                    "Baixa": "#6bcf7f"
                }
            )
            st.plotly_chart(fig, use_container_width=True)

def generate_ai_insights(client_data):
    """Gerar insights baseados no perfil do cliente"""
    
    # Aqui seria a lógica real de IA
    # Por ora, vamos simular baseado no perfil
    
    setor = client_data['setor']
    desafios = client_data['desafios']
    orcamento = client_data['orcamento']
    objetivo = client_data['objetivo_principal']
    
    insights = {
        "pontos_fortes": [],
        "oportunidades": [],
        "riscos": [],
        "recomendacoes": [],
        "estrategias": [],
        "metricas": []
    }
    
    # Lógica baseada no setor
    if setor == "Representação Comercial":
        insights["pontos_fortes"] = [
            "Experiência em múltiplos canais de vendas",
            "Relacionamento com clientes B2B estabelecido",
            "Conhecimento de ciclos de vendas complexos"
        ]
        insights["oportunidades"] = [
            "Automação de processos de geração de leads",
            "Implementação de CRM avançado",
            "Otimização do funil de vendas B2B",
            "Desenvolvimento de conteúdo técnico"
        ]
        insights["recomendacoes"] = [
            "Foco em LinkedIn e marketing B2B",
            "Implementar lead scoring automatizado", 
            "Criar conteúdo educativo para prospects",
            "Desenvolver parcerias estratégicas"
        ]
    
    elif setor == "E-commerce/Varejo Online":
        insights["oportunidades"] = [
            "Otimização de campanhas de Google Ads",
            "Remarketing para carrinho abandonado",
            "Automação de email marketing",
            "Implementação de reviews e social proof"
        ]
    
    # Baseado nos desafios
    if "Baixa geração de leads" in desafios:
        insights["estrategias"].append("Implementar funil de lead magnets")
        insights["estrategias"].append("Otimizar SEO para busca orgânica")
    
    if "Conversão baixa" in desafios:
        insights["estrategias"].append("A/B testing em landing pages")
        insights["estrategias"].append("Otimização da jornada do cliente")
    
    return insights

def show_detailed_insights(insights):
    """Mostrar insights detalhados"""
    
    # Análise SWOT
    st.markdown("### 🎯 **Análise Estratégica**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### ✅ **Pontos Fortes Identificados**")
        for ponto in insights.get("pontos_fortes", ["Análise em andamento..."]):
            st.success(f"• {ponto}")
        
        st.markdown("#### 🚀 **Oportunidades**") 
        for oportunidade in insights.get("oportunidades", ["Identificando oportunidades..."]):
            st.info(f"• {oportunidade}")
    
    with col2:
        st.markdown("#### ⚠️ **Riscos e Desafios**")
        riscos = insights.get("riscos", [
            "Concorrência acirrada no setor",
            "Necessidade de investimento em tecnologia",
            "Curva de aprendizado para novas ferramentas"
        ])
        for risco in riscos:
            st.warning(f"• {risco}")
        
        st.markdown("#### 💡 **Recomendações Prioritárias**")
        for rec in insights.get("recomendacoes", ["Gerando recomendações..."]):
            st.success(f"• {rec}")

def generate_proposal():
    """Gerar proposta de marketing"""
    
    st.markdown("## 📋 **Gerador de Propostas**")
    
    if 'current_client' not in st.session_state:
        st.warning("⚠️ Nenhum cliente carregado.")
        return
    
    if 'current_analysis' not in st.session_state:
        st.warning("⚠️ Execute a análise do cliente primeiro.")
        return
    
    client = st.session_state['current_client']
    analysis = st.session_state['current_analysis']
    
    st.markdown(f"### 📄 **Proposta para: {client['nome']}**")
    
    if st.button("📋 Gerar Proposta Completa"):
        with st.spinner("🔄 Gerando proposta personalizada..."):
            import time
            time.sleep(3)
        
        # Gerar proposta baseada na análise
        show_generated_proposal(client, analysis)

def show_generated_proposal(client, analysis):
    """Mostrar proposta gerada"""
    
    st.markdown("## 📋 **Proposta de Marketing Personalizada**")
    
    scores = analysis['scores']
    insights = analysis['insights']
    recommendations = analysis['recommendations']
    
    # Header da proposta
    st.markdown(f"""
    ### 🎯 **Plano Estratégico de Marketing**
    **Cliente:** {client['nome']}  
    **Setor:** {client['setor']}  
    **Objetivo:** {client['objetivo_principal']}  
    **Prazo:** {client['prazo']}  
    **Data:** {datetime.now().strftime('%d/%m/%Y')}
    """)
    
    # Resumo executivo
    st.markdown("### 📊 **Resumo Executivo**")
    st.info(f"""
    Com base na análise detalhada do perfil de **{client['nome']}**, identificamos oportunidades significativas 
    para otimização de resultados no setor de **{client['setor']}**. 
    
    **Score de Potencial:** {scores['potential_score']:.1f}/10  
    **ROI Projetado:** {scores['roi_projection']} em {scores['time_to_results']}  
    **Investimento Sugerido:** {client['orcamento']} mensal  
    **Probabilidade de Sucesso:** {scores['success_probability']}
    """)
    
    # Estratégias baseadas nos insights da IA
    st.markdown("### 🚀 **Estratégias Recomendadas**")
    
    # Pegar insights de alta prioridade para estratégias
    high_priority_insights = [i for i in insights if i.prioridade == "Alta"]
    
    for i, insight in enumerate(high_priority_insights[:3], 1):
        with st.expander(f"📌 Estratégia {i}: {insight.titulo}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Descrição:** {insight.descricao}")
                st.write(f"**Implementação:** {insight.prazo_implementacao}")
                st.write(f"**Complexidade:** {insight.complexidade}")
            
            with col2:
                st.metric("� Impacto", insight.impacto_estimado)
                st.metric("🎯 Prioridade", insight.prioridade)
                st.metric("⏰ Prazo", insight.prazo_implementacao)
    
    # Cronograma baseado nos insights
    st.markdown("### 📅 **Cronograma de Implementação**")
    
    cronograma_data = {
        "Fase": [
            "1. Setup e Planejamento",
            "2. Implementação Inicial", 
            "3. Otimização Contínua",
            "4. Expansão de Canais",
            "5. Análise e Ajustes"
        ],
        "Período": ["Semana 1-2", "Semana 3-8", "Semana 9-16", "Semana 17-20", "Semana 21-24"],
        "Atividades": [
            "Configuração inicial, definição de KPIs",
            "Implementar estratégias prioritárias",
            "A/B testing, otimização de campanhas", 
            "Novos canais, scaling de sucesso",
            "Relatórios, ajustes estratégicos"
        ],
        "Status": ["✅", "🔄", "⏳", "⏳", "⏳"]
    }
    
    df_cronograma = pd.DataFrame(cronograma_data)
    st.dataframe(df_cronograma, use_container_width=True)
    
    # Investimento
    st.markdown("### 💰 **Resumo do Investimento**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📊 Setup Inicial", "R$ 5.000", "Uma vez")
    
    with col2:
        st.metric("🔄 Mensal", client['orcamento'], "Recorrente")
    
    with col3:
        st.metric("📈 ROI Esperado", scores['roi_projection'], scores['time_to_results'])
    
    # Métricas de acompanhamento
    st.markdown("### 📊 **Métricas de Acompanhamento**")
    
    metrics = analysis['success_metrics']
    if metrics:
        metrics_df = pd.DataFrame(metrics)
        st.dataframe(metrics_df, use_container_width=True)
    
    # Recomendações principais
    st.markdown("### 💡 **Próximos Passos**")
    
    for i, rec in enumerate(recommendations[:5], 1):
        st.success(f"{i}. {rec}")
    
    # Botões de ação
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📱 Gerar Apresentação"):
            st.success("🎯 Apresentação gerada! (Funcionalidade em desenvolvimento)")
    
    with col2:
        if st.button("📧 Enviar por Email"):
            st.success("📧 Email enviado! (Funcionalidade em desenvolvimento)")
    
    with col3:
        if st.button("💾 Salvar Proposta"):
            st.success("💾 Proposta salva nos clientes!")

def get_strategies_for_sector(setor):
    """Obter estratégias baseadas no setor"""
    
    if setor == "Representação Comercial":
        return [
            {
                "nome": "Automação de Lead Generation B2B",
                "descricao": "Implementação de sistema automatizado para captura e qualificação de leads B2B",
                "implementacao": "LinkedIn Sales Navigator + HubSpot + Email sequences",
                "investimento": "R$ 15.000",
                "roi": "200%",
                "prazo": "3 meses"
            },
            {
                "nome": "Otimização do Funil de Vendas", 
                "descricao": "Reestruturação do processo de vendas com foco em conversão",
                "implementacao": "CRM personalizado + Lead scoring + Follow-up automatizado",
                "investimento": "R$ 20.000",
                "roi": "150%", 
                "prazo": "4 meses"
            },
            {
                "nome": "Conteúdo Estratégico B2B",
                "descricao": "Desenvolvimento de conteúdo técnico para educação de prospects",
                "implementacao": "Blog técnico + Webinars + Cases de sucesso",
                "investimento": "R$ 10.000",
                "roi": "180%",
                "prazo": "6 meses"
            }
        ]
    
    else:
        return [
            {
                "nome": "Estratégia Digital Completa",
                "descricao": "Implementação de marketing digital integrado",
                "implementacao": "Google Ads + Facebook Ads + Email Marketing",
                "investimento": "R$ 25.000",
                "roi": "160%",
                "prazo": "4 meses"
            }
        ]

def show_saved_clients():
    """Mostrar clientes salvos"""
    st.markdown("## 👥 **Clientes Salvos**")
    st.info("📝 Funcionalidade em desenvolvimento - Histórico de clientes analisados")

def show_knowledge_base():
    """Base de conhecimento"""
    st.markdown("## 📚 **Base de Conhecimento**")
    
    st.markdown("""
    ### 🎯 **Como usar o Assistente**
    
    1. **📝 Novo Cliente:** Colete todos os dados necessários do cliente
    2. **📊 Análise:** Execute a análise IA para gerar insights
    3. **📋 Proposta:** Gere uma proposta personalizada 
    4. **🎯 Apresentação:** Use os materiais para apresentar ao cliente
    
    ### 💡 **Dicas de Consultoria**
    
    - Sempre confirme informações com o cliente antes da análise
    - Use os insights gerados como base, mas adicione sua experiência
    - Personalize a proposta com casos específicos do setor
    - Acompanhe os resultados e ajuste estratégias conforme necessário
    """)

if __name__ == "__main__":
    main()