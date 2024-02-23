import unittest

from sssm.calculate_pe_ratio import calculate_pe_ratio


class TestCalculatePERatio(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.zero_price_value = 0
        cls.positive_price_value = 10
        cls.negative_price_value = -10
        cls.positive_dividend = 10
        cls.zero_dividend = 0
        cls.negative_dividend = -10
        cls.par_value = 1
        cls.expected_dividend_yield1 = 0
        cls.expected_dividend_yield2 = 1

    def test_case_ideal(self):
        self.assertEqual(
            calculate_pe_ratio(
                self.positive_price_value,
                self.positive_dividend,
            ),
            self.expected_dividend_yield2
        )

    def test_case_zero_price(self):
        self.assertEqual(
            calculate_pe_ratio(
                self.zero_price_value,
                self.positive_dividend,
            ),
            self.expected_dividend_yield1
        )

    def test_case_zero_dividend(self):
        self.assertEqual(
            calculate_pe_ratio(
                self.positive_price_value,
                self.zero_dividend,
            ),
            self.expected_dividend_yield1
        )

    def test_case_negative_price(self):
        self.assertRaises(
            ValueError,
            calculate_pe_ratio,
            self.negative_price_value,
            self.positive_dividend
        )

    def test_case_negative_dividend(self):
        self.assertRaises(
            ValueError,
            calculate_pe_ratio,
            self.positive_price_value,
            self.negative_dividend
        )


if __name__ == '__main__':
    unittest.main()
