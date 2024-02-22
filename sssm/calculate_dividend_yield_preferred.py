def calculate_dividend_yield_preferred(price: float | int, fixed_dividend: float | int,
                                       par_value: float | int) -> float:
    if price < 0:
        raise ValueError("price cannot be negative")
    if price == 0:
        return 0
    return (fixed_dividend * par_value)/price
