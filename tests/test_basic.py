# content of test_sample.py

from sample.helpers import get_tidy_data_path
import pandas as pd


def test_check_dataframe_size():
    df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')
    assert df.shape[1] == 26

