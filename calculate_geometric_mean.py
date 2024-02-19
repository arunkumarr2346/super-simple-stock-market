import pandas as pd


def calculate_geometric_mean(price: pd.Series) -> float:
    """

    :param price:
    :return:
    """
    if not isinstance(price, pd.Series):
        raise TypeError("price must be a pandas series datatype")
    if price.empty:
        raise ValueError("cannot compute geometric mean as price is empty")
    return pow(price.product(), (1/price.shape[0]))

