import numpy as np
import unittest

import pandas as pd

from sssm.calculate_geometric_mean import calculate_geometric_mean


class TestCalculateVolumeWeightPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.empty_price = pd.Series(dtype=np.float64)
        cls.valid_price = pd.Series(range(1, 10))
        cls.expected_geometric_mean = 4.147

    def test_case_ideal(self):
        self.assertEqual(
            round(
                calculate_geometric_mean(
                    self.valid_price,
                ), 3
            ),
            self.expected_geometric_mean
        )

    def test_case_empty_price(self):
        self.assertRaises(
            ValueError,
            calculate_geometric_mean,
            self.empty_price
        )

    def test_case_non_series_price(self):
        self.assertRaises(
            TypeError,
            calculate_geometric_mean,
            []
        )


if __name__ == '__main__':
    unittest.main()
