import unittest

from sssm.calculate_dividend_yield_preferred import calculate_dividend_yield_preferred


class TestCalculateDividendYieldPreferred(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.zero_price_value = 0
        cls.positive_price_value = 10
        cls.negative_price_value = -10
        cls.fixed_dividend = 10
        cls.par_value = 1
        cls.expected_dividend_yield1 = 0
        cls.expected_dividend_yield2 = 1

    def test_case_ideal(self):
        self.assertEqual(
            calculate_dividend_yield_preferred(
                self.positive_price_value,
                self.fixed_dividend,
                self.par_value
            ),
            self.expected_dividend_yield2
        )

    def test_case_zero_price(self):
        self.assertEqual(
            calculate_dividend_yield_preferred(
                self.zero_price_value,
                self.fixed_dividend,
                self.par_value
            ),
            self.expected_dividend_yield1
        )

    def test_case_negative_price(self):
        self.assertRaises(
            ValueError,
            calculate_dividend_yield_preferred,
            self.negative_price_value,
            self.fixed_dividend,
            self.par_value
        )


if __name__ == '__main__':
    unittest.main()
