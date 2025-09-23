import pytest
from services.data.data_processor import DataProcessor
import pandas as pd

def test_load_csv_data():
    from io import StringIO
    processor = DataProcessor()
    csv = 'col1,col2\n1,2\n3,4'
    df = processor.load_csv_data(StringIO(csv))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_clean_data():
    processor = DataProcessor()
    df = pd.DataFrame({'A': ['  a ', 'b  '], 'B': [1, 2]})
    cleaned = processor.clean_data(df)
    assert 'a' in cleaned.columns
    assert cleaned['a'].iloc[0] == 'a'
