def calculate_pe_ratio(price: int | float, dividend: int | float) -> float:
    if price == 0:
        return 0
    if price < 0:
        raise ValueError("price cannot be negative")
    if dividend == 0:
        return 0
    if dividend < 0:
        raise ValueError("dividend cannot be negative")
    return price/dividend

