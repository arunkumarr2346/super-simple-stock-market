import pandas as pd

from sssm.calculate_geometric_mean import calculate_geometric_mean
from sssm.constants import FieldNames


def calculate_gbce_all_share_index(df: pd.DataFrame) -> float:
    if FieldNames.TRADED_PRICE not in df.columns:
        raise ValueError("traded price not present in dataframe")
    if FieldNames.STOCK_SYMBOL not in df.columns:
        raise ValueError("stock symbol not present in dataframe")
    df = df.drop_duplicates(subset=[FieldNames.STOCK_SYMBOL], keep='last')
    return calculate_geometric_mean(price=df[FieldNames.TRADED_PRICE])
