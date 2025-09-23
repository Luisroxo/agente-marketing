from services.data.data_processor import DataProcessor
from services.analysis.analysis_service import AnalysisService
from services.reporting.reporting_service import ReportingService


def test_full_data_flow():
    # Simula fluxo completo: carregar, analisar, gerar relatório
    from io import StringIO

    processor = DataProcessor()
    csv = "col1,col2\n1,2\n3,4"
    df = processor.load_csv_data(StringIO(csv))
    cleaned = processor.clean_data(df)
    analysis = AnalysisService()
    analysis.set_data(cleaned)
    stats = analysis.descriptive_statistics()
    report = ReportingService()
    report.set_data(cleaned)
    summary = report.generate_executive_summary()
    assert isinstance(stats, dict)
    assert isinstance(summary, str)
    assert "col1" in cleaned.columns or "col1" in stats
