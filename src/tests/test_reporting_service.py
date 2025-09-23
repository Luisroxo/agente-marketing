from services.reporting.reporting_service import ReportingService
import pandas as pd


def test_set_data():
    service = ReportingService()
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    service.set_data(df)
    assert service.data is not None
    assert service.data.shape == (2, 2)


def test_generate_executive_summary():
    service = ReportingService()
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    service.set_data(df)
    summary = service.generate_executive_summary()
    assert isinstance(summary, str)
