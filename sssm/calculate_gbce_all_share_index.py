import pandas as pd

from calculate_geometric_mean import calculate_geometric_mean
from constants import FieldNames


def calculate_gbce_all_share_index(df: pd.DataFrame) -> float:
    df = df.drop_duplicates(subset=[FieldNames.STOCK_SYMBOL], keep='last')
    return calculate_geometric_mean(price=df[FieldNames.TRADED_PRICE])
