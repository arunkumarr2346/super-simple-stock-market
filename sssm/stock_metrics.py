from datetime import datetime, timedelta

import pandas as pd

from sssm.calculate_dividend_yield_common import calculate_dividend_yield_common
from sssm.calculate_dividend_yield_preferred import calculate_dividend_yield_preferred
from sssm.calculate_pe_ratio import calculate_pe_ratio
from sssm.calculate_volume_weighted_stock_price import calculate_volume_weighted_stock_price
from sssm.constants import FieldNames, TransactionType, StockTypes


class StockMetrics:

    def __init__(self, stock_symbol, price, gbce_ref_df: pd.DataFrame, gbce_transaction_df: pd.DataFrame) -> None:
        self._stock_symbol = stock_symbol
        if not isinstance(price, (float, int)):
            raise TypeError(f"price can only be an int or float received: {type(price)}")
        self._price = price
        self._gbce_ref_df = gbce_ref_df
        self._gbce_transaction_df = gbce_transaction_df

    def __repr__(self) -> str:
        return f"""stock symbol: {self._stock_symbol}
stock price: {self._price}
dividend yield: {self.dividend_yield()}
p/e ratio: {self.pe_ratio()}
volume weighted stock price: {self.volume_weighted_stock_price()}
"""

    def record_trade(self, share_quantity: int, transaction_type: str, traded_price: float):
        if transaction_type not in (TransactionType.BUY, TransactionType.SELL):
            raise TypeError(f"cannot record trade invalid transaction type provide: {transaction_type}")
        if share_quantity - int(share_quantity) > 0:
            raise ValueError(f"share quantity can only be integer")
        if share_quantity == 0:
            raise ValueError(f"share quantity can only be integer")
        if share_quantity < 0:
            raise ValueError(f"share quantity can only be positive integer")
        self._gbce_transaction_df.loc[self._gbce_transaction_df.shape[0]] = pd.Series(
                {
                    FieldNames.STOCK_SYMBOL: self._stock_symbol,
                    FieldNames.TRANSACTION_TYPE: transaction_type,
                    FieldNames.QUANTITY: share_quantity,
                    FieldNames.TRADED_PRICE: traded_price,
                    FieldNames.TRANSACTION_TIMESTAMP: datetime.now(),
                }
            )

    def dividend_yield(self):
        df = self._gbce_ref_df[self._gbce_ref_df[FieldNames.STOCK_SYMBOL] == self._stock_symbol]
        if df.empty:
            return 0
        stock_type = df[FieldNames.STOCK_TYPE].values[0]
        if stock_type == StockTypes.PREFERRED:
            return calculate_dividend_yield_preferred(
                price=self._price,
                fixed_dividend=df[FieldNames.FIXED_DIVIDEND].values[0],
                par_value=df[FieldNames.PAR_VALUE].values[0],
            )
        elif stock_type == StockTypes.COMMON:
            return calculate_dividend_yield_common(
                price=self._price,
                last_dividend=df[FieldNames.LAST_DIVIDEND].values[0],
            )
        else:
            raise TypeError(f"stock type: {stock_type} is not configured or is invalid")

    def pe_ratio(self):
        df = self._gbce_ref_df[self._gbce_ref_df[FieldNames.STOCK_SYMBOL] == self._stock_symbol]
        if df.empty:
            return 0
        return calculate_pe_ratio(
            price=self._price,
            dividend=df[FieldNames.LAST_DIVIDEND].values[0],
        )

    def volume_weighted_stock_price(self):
        df = self._gbce_transaction_df[
            (self._gbce_transaction_df[FieldNames.STOCK_SYMBOL] == self._stock_symbol) &
            (self._gbce_transaction_df[FieldNames.TRANSACTION_TIMESTAMP] > (datetime.now() - timedelta(minutes=15)))
        ]
        if df.empty:
            raise ValueError("cannot calculate volume weighted stock price as no trades occurred in the past 15 minutes")
        return calculate_volume_weighted_stock_price(
            traded_price=df[FieldNames.TRADED_PRICE],
            quantity=df[FieldNames.QUANTITY]
        )

