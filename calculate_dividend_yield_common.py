def calculate_dividend_yield_common(price: float | int, last_dividend: float | int) -> float:
    if price < 0:
        raise ValueError("price cannot be negative")
    if price == 0:
        return 0
    return last_dividend/price
