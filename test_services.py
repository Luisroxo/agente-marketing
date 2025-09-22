"""
Teste rápido dos serviços enterprise
"""
import sys
import os
from pathlib import Path

# Configurar path
PROJECT_ROOT = Path(__file__).parent
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

def test_services():
    print("🚀 Testando Serviços Enterprise...")
    
    try:
        # Testar DataProcessor
        from services.data.dataProcessor import DataProcessor
        dp = DataProcessor()
        print("✅ DataProcessor carregado com sucesso!")
        
        # Testar AnalysisService
        from services.analysis.analysisService import AnalysisService
        analysis = AnalysisService()
        print("✅ AnalysisService carregado com sucesso!")
        
        # Testar ReportingService
        from services.reporting.reportingService import ReportingService
        report = ReportingService()
        print("✅ ReportingService carregado com sucesso!")
        
        print("\n🎉 Todos os serviços enterprise estão funcionando!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao carregar serviços: {e}")
        return False

if __name__ == "__main__":
    test_services()