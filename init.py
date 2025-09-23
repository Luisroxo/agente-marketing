"""
Script de inicialização e teste do projeto
"""
import os
import sys
import subprocess
from pathlib import Path

def test_imports():
    """Testar se os módulos podem ser importados"""
    print("🧪 Testando imports dos módulos...")
    
    try:
        # Teste básico dos módulos
        sys.path.append(str(Path(__file__).parent))
        try:
            from src.services.data.dataProcessor import DataProcessor
            print("✅ src.services.data.dataProcessor")

            from src.services.analysis.statisticalAnalysis import BasicAnalyzer
            print("✅ src.services.analysis.statisticalAnalysis")

            from src.services.reporting.reportGenerator import ReportGenerator
            print("✅ src.services.reporting.reportGenerator")

            from src.services.external.googleSheetsService import GoogleSheetsIntegration
            print("✅ src.services.external.googleSheetsService")

            from src.services.data.helpers import generate_sample_data
            print("✅ src.services.data.helpers")

            return True
        except ImportError as e:
            print(f"❌ Erro de importação: {e}")
            return False

def test_data_processing():
    """Testar processamento de dados"""
    print("\n📊 Testando processamento de dados...")
    
    try:
        from src.services.data.helpers import generate_sample_data
        from src.services.data.dataProcessor import DataProcessor
        from src.services.analysis.statisticalAnalysis import BasicAnalyzer
        
        # Gerar dados de teste
        df = generate_sample_data()
        print(f"✅ Dados de exemplo gerados: {len(df)} registros")
        
        # Testar processador
        processor = DataProcessor()
        summary = processor.get_data_summary(df)
        print(f"✅ Resumo dos dados: {summary['total_rows']} linhas, {summary['total_columns']} colunas")
        
        # Testar analisador
        analyzer = BasicAnalyzer()
        analyzer.set_data(df)
        insights = analyzer.generate_insights()
        print(f"✅ Insights gerados: {len(insights)} descobertas")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste de processamento: {e}")
        return False

def create_test_run():
    """Criar arquivo de teste rápido"""
    test_content = '''

    import pandas as pd
    import sys
    from pathlib import Path

    # Adicionar diretório ao path
    sys.path.append(str(Path(__file__).parent))

    from src.services.data.helpers import generate_sample_data
    from src.services.analysis.statisticalAnalysis import BasicAnalyzer
    from src.services.reporting.reportGenerator import ReportGenerator


def main():
    print("🚀 Teste rápido do Agente de IA para Marketing")
    print("=" * 50)
    
    # Gerar dados de teste
    df = generate_sample_data()
    print(f"📊 Dados gerados: {len(df)} registros")
    
    # Análise básica
    analyzer = BasicAnalyzer()
    analyzer.set_data(df)
    insights = analyzer.generate_insights()
    
    print("\\n💡 Insights encontrados:")
    for insight in insights:
        print(f"  • {insight}")
    
    # Gerar relatório
    report_gen = ReportGenerator()
    report_gen.set_data(df)
    report = report_gen.generate_executive_summary()
    
    print("\\n📄 Resumo executivo gerado com sucesso!")
    print("✅ Teste concluído com sucesso!")

if __name__ == "__main__":
    main()
'''
    
    with open("test_quick.py", "w", encoding="utf-8") as f:
        f.write(test_content)
    
    print("✅ Arquivo test_quick.py criado")

def main():
    """Função principal"""
    print("🤖 Agente de IA para Marketing - Inicialização")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not Path("app.py").exists():
        print("❌ Execute este script no diretório do projeto")
        return
    
    # Testar imports
    if not test_imports():
        print("\n❌ Falha nos testes de importação")
        print("💡 Instale as dependências: pip install -r requirements.txt")
        return
    
    # Testar processamento
    if not test_data_processing():
        print("\n❌ Falha nos testes de processamento")
        return
    
    # Criar teste rápido
    create_test_run()
    
    print("\n" + "=" * 50)
    print("✅ Inicialização concluída com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Instalar dependências: pip install -r requirements.txt")
    print("2. Executar aplicação: python run.py")
    print("3. Ou testar módulos: python test_quick.py")
    print("4. Ou executar direto: streamlit run app.py")

if __name__ == "__main__":
    main()