def calculate_lumpsum(principal, annual_rate_percent, years):
    """
    Calculate the future value of a lumpsum investment using compound interest.

    Args:
        principal (float): Initial investment amount.
        annual_rate_percent (float): Expected annual return rate in percent.
        years (float): Duration of investment in years.

    Returns:
        dict: Contains maturity amount, total investment, and profit earned.
    """
    r = annual_rate_percent / 100
    t = years

    maturity_amount = principal * (1 + r) ** t
    profit = maturity_amount - principal

    return {
        "maturity_amount": round(maturity_amount, 2),
        "total_investment": round(principal, 2),
        "profit": round(profit, 2)
    }

if __name__ == "__main__":
    # Example usage
    result = calculate_lumpsum(principal=200000, annual_rate_percent=12, years=10)

    print("Lumpsum Investment Calculator Example")
    print("-------------------------------------")
    print(f"Maturity Amount   : ₹{result['maturity_amount']}")
    print(f"Total Investment  : ₹{result['total_investment']}")
    print(f"Profit Earned     : ₹{result['profit']}")
