import numpy as np
import unittest

import pandas as pd

from sssm.calculate_volume_weighted_stock_price import calculate_volume_weighted_stock_price


class TestCalculateVolumeWeightPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.empty_traded_price = pd.Series(dtype=np.float64)
        cls.empty_quantity = pd.Series(dtype=np.float64)
        cls.valid_traded_price = pd.Series(range(10))
        cls.valid_quantity = pd.Series(range(10))
        cls.expected_volume_weighted_stock_price1 = 6.33
        cls.expected_volume_weighted_stock_price2 = 0

    def test_case_ideal(self):
        self.assertEqual(
            round(
                calculate_volume_weighted_stock_price(
                    self.valid_traded_price,
                    self.valid_quantity,
                ), 2
            ),
            self.expected_volume_weighted_stock_price1
        )

    def test_case_empty_traded_price(self):
        self.assertEqual(
            calculate_volume_weighted_stock_price(
                self.empty_traded_price,
                self.valid_quantity,
            ),
            self.expected_volume_weighted_stock_price2
        )

    def test_case_empty_quantity(self):
        self.assertRaises(
            ValueError,
            calculate_volume_weighted_stock_price,
            self.valid_traded_price,
            self.empty_quantity
        )

    def test_case_non_series_traded_price(self):
        self.assertRaises(
            TypeError,
            calculate_volume_weighted_stock_price,
            self.valid_traded_price,
            []
        )

    def test_case_non_series_quantity(self):
        self.assertRaises(
            TypeError,
            calculate_volume_weighted_stock_price,
            [],
            self.valid_quantity
        )


if __name__ == '__main__':
    unittest.main()
