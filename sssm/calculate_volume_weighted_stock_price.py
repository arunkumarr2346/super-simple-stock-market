import pandas as pd


def calculate_volume_weighted_stock_price(traded_price: pd.Series, quantity: pd.Series) -> float:
    if not isinstance(traded_price, pd.Series):
        raise TypeError("traded_price must be a pandas series datatype")
    if not isinstance(quantity, pd.Series):
        raise TypeError("quantity must be a pandas series datatype")
    # if traded_price.empty:
    #     return 0
    if quantity.empty:
        raise ValueError("quantity must not be empty")
    return (traded_price * quantity).sum() / quantity.sum()
