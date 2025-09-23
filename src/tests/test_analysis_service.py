from services.analysis.analysis_service import AnalysisService
import pandas as pd


def test_set_data():
    service = AnalysisService()
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    service.set_data(df)
    assert service.data is not None
    assert service.data.shape == (2, 2)


def test_descriptive_statistics():
    service = AnalysisService()
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    service.set_data(df)
    stats = service.descriptive_statistics()
    assert "A" in stats
    assert "B" in stats
