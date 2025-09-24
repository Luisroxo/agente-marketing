import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from services.data.data_processor import DataProcessor
import pandas as pd

def test_load_csv_data():
    processor = DataProcessor()
    csv = 'col1,col2\n1,2\n3,4'
    df = processor.load_csv_data(csv)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_clean_data():
    processor = DataProcessor()
    df = pd.DataFrame({'A': ['  a ', 'b  '], 'B': [1, 2]})
    cleaned = processor.clean_data(df)
    assert 'A' in cleaned.columns
    assert cleaned['A'].iloc[0] == 'a'
