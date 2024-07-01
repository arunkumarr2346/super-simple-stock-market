#  Assignment Solution – Super Simple Stock Market

Provide working source code that will 

a. For a given stock, 

i. Given any price as input, calculate the dividend yield

ii. Given any price as input, calculate the P/E Ratio

iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price

iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes

b. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Usage
Create an object for the stock metrics.

```python
import pandas as pd 

from sssm.stock_metrics import StockMetrics
from sssm.constants import FieldNames

gbce_ref_df_data = pd.read_csv(r"./sssm/gbce_ref_processed.csv")
gbce_transaction_df_data = pd.DataFrame(
    columns=[
        FieldNames.STOCK_SYMBOL, FieldNames.QUANTITY, FieldNames.TRANSACTION_TYPE,
        FieldNames.TRADED_PRICE, FieldNames.TRANSACTION_TIMESTAMP
    ],
)
s = StockMetrics(
    stock_symbol="ALE",
    price=95,
    gbce_ref_df=gbce_ref_df_data,
    gbce_transaction_df=gbce_transaction_df_data,
)
```
To get dividend yield. 
```python
print(s.dividend_yield())
```
To get P/E Ratio.
```python
print(s.pe_ratio())
```
To record a new trade 
```python
from sssm.constants import TransactionType

s.record_trade(
    share_quantity=20,
    transaction_type=TransactionType.BUY,
    traded_price=100,
)
```
To get the Volume Weighted Stock Price based on trades in past 15 minutes.
```python
print(s.volume_weighted_stock_price())
```
To get the GBCE All Share Index.

```python
from random import randint
from sssm.calculate_gbce_all_share_index import calculate_gbce_all_share_index
from sssm.stock_metrics import StockMetrics
from sssm.constants import TransactionType

# add random trades for all share index
for symbol in gbce_ref_df_data[FieldNames.STOCK_SYMBOL].tolist():
    r1 = randint(5, 15)
    p1 = randint(50, 100)
    s = StockMetrics(
        stock_symbol=symbol,
        price=p1,
        gbce_ref_df=gbce_ref_df_data,
        gbce_transaction_df=gbce_transaction_df_data,
    )
    for i in range(1, r1):
        s.record_trade(
            share_quantity=i,
            transaction_type=TransactionType.BUY,
            traded_price=p1 + i,
        )
    print(s)

print(calculate_gbce_all_share_index(gbce_transaction_df_data))
```

## License

JPMorgan Chase & Co Unauthorized reproduction or distribution of all or any of this material is strictly prohibited.
