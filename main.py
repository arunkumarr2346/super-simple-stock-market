from random import random, randint

import pandas as pd

from calculate_gbce_all_share_index import calculate_gbce_all_share_index
from calculate_geometric_mean import calculate_geometric_mean
from constants import FieldNames
from stock_metrics import StockMetrics

# gbce_ref_df_data = pd.DataFrame(
#     [
#         {
#             'stock_symbol': 'TEA',
#             'stock_type': 'Common',
#             'last_dividend': 0,
#             'par_value': 100
#         },
#         {
#             'stock_symbol': 'POP',
#             'stock_type': 'Common',
#             'last_dividend': 8,
#             'par_value': 100
#         },
#         {
#             'stock_symbol': 'ALE',
#             'stock_type': 'Common',
#             'last_dividend': 23,
#             'par_value': 60
#          },
#         {
#             'stock_symbol': 'GIN',
#             'stock_type': 'Preferred',
#             'last_dividend': 8,
#             'par_value': 100,
#             'fixed_dividend': 2.0
#          },
#         {
#             'stock_symbol': 'JOE',
#             'stock_type': 'Common',
#             'last_dividend': 13,
#             'par_value': 250,
#             'fixed_dividend': ' '
#          },
#         {
#             'stock_symbol': 'AAA',
#             'stock_type': 'Common',
#             'last_dividend': " ",
#             'par_value': " "
#         }
#     ]
# )

gbce_ref_df_data = pd.read_csv("gbce_ref_raw.csv")
gbce_transaction_df_data = pd.DataFrame(
    columns=[FieldNames.STOCK_SYMBOL, FieldNames.QUANTITY, FieldNames.TRANSACTION_TYPE, FieldNames.TRADED_PRICE,
             FieldNames.TRANSACTION_TIMESTAMP],
)

# data cleanup and streamlining
gbce_ref_df_data[FieldNames.STOCK_TYPE] = gbce_ref_df_data[FieldNames.STOCK_TYPE].str.lower()
gbce_ref_df_data[FieldNames.LAST_DIVIDEND] = \
    gbce_ref_df_data[FieldNames.LAST_DIVIDEND].replace(regex=r"\D", value="").replace("", 0).fillna(0)
gbce_ref_df_data[FieldNames.PAR_VALUE] = \
    gbce_ref_df_data[FieldNames.PAR_VALUE].replace(regex=r"\D", value="").replace("", 0).fillna(0)
gbce_ref_df_data[FieldNames.FIXED_DIVIDEND] = \
    gbce_ref_df_data[FieldNames.FIXED_DIVIDEND].replace(regex=r"\D", value="").replace("", 0).fillna(0)
gbce_ref_df_data[FieldNames.LAST_DIVIDEND] = gbce_ref_df_data[FieldNames.LAST_DIVIDEND].astype(float)
gbce_ref_df_data[FieldNames.PAR_VALUE] = gbce_ref_df_data[FieldNames.PAR_VALUE].astype(float)
gbce_ref_df_data[FieldNames.FIXED_DIVIDEND] = gbce_ref_df_data[FieldNames.FIXED_DIVIDEND].astype(float)
gbce_ref_df_data[FieldNames.FIXED_DIVIDEND] = gbce_ref_df_data[FieldNames.FIXED_DIVIDEND]/100  # percent to decimal

# gbce_ref_df_data.to_csv("gbce_ref_processed.csv", index=False)

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
            transaction_type="buy",
            traded_price=p1+i,
        )
    # s.volume_weighted_stock_price()
    print(s)


print(calculate_gbce_all_share_index(gbce_transaction_df_data))

