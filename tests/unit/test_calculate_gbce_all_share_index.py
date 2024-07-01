import unittest

import pandas as pd

from sssm.calculate_gbce_all_share_index import calculate_gbce_all_share_index
from sssm.constants import FieldNames


class TestCalculateGBCEAllShareIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.empty_df_with_necessary_columns = pd.DataFrame(
            columns=[FieldNames.TRADED_PRICE, FieldNames.STOCK_SYMBOL]
        )
        cls.empty_df_without_necessary_columns = pd.DataFrame()
        cls.empty_df_without_traded_price = pd.DataFrame(
            columns=[FieldNames.STOCK_SYMBOL]
        )
        cls.empty_df_without_stock_symbol = pd.DataFrame(
            columns=[FieldNames.TRADED_PRICE]
        )
        cls.df = pd.DataFrame(
            {
                FieldNames.STOCK_SYMBOL: ['TEA', 'TEA', 'ALE', 'ALE', 'JOE'],
                FieldNames.TRADED_PRICE: [100, 250, 60, 100, 150],
             }
        )
        cls.expected_output1 = 155.362

    def test_case_ideal(self):
        self.assertEqual(
            round(calculate_gbce_all_share_index(self.df), 3),
            self.expected_output1
        )

    def test_case_empty_df_with_necessary_columns(self):
        self.assertRaises(
            ValueError,
            calculate_gbce_all_share_index,
            self.empty_df_with_necessary_columns
        )

    def test_case_empty_df_without_traded_price(self):
        self.assertRaises(
            ValueError,
            calculate_gbce_all_share_index,
            self.empty_df_without_traded_price
        )

    def test_empty_df_without_stock_symbol(self):
        self.assertRaises(
            ValueError,
            calculate_gbce_all_share_index,
            self.empty_df_without_stock_symbol
        )

    def test_case_df_without_traded_price(self):
        self.assertRaises(
            ValueError,
            calculate_gbce_all_share_index,
            self.df[[FieldNames.STOCK_SYMBOL]]
        )

    def test_df_without_stock_symbol(self):
        self.assertRaises(
            ValueError,
            calculate_gbce_all_share_index,
            self.df[[FieldNames.TRADED_PRICE]]
        )


if __name__ == '__main__':
    unittest.main()
