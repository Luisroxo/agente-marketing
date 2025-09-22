
import pandas as pd
import sys
from pathlib import Path

# Adicionar diretório ao path
sys.path.append(str(Path(__file__).parent))

from utils.helpers import generate_sample_data
from analysis.basic_analysis import BasicAnalyzer
from templates.report_generator import ReportGenerator

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
    
    print("\n💡 Insights encontrados:")
    for insight in insights:
        print(f"  • {insight}")
    
    # Gerar relatório
    report_gen = ReportGenerator()
    report_gen.set_data(df)
    report = report_gen.generate_executive_summary()
    
    print("\n📄 Resumo executivo gerado com sucesso!")
    print("✅ Teste concluído com sucesso!")

if __name__ == "__main__":
    main()
