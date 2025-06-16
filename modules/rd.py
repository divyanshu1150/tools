def calculate_rd(monthly_deposit, annual_rate_percent, years, compounding_frequency=4):
    """
    Calculate the maturity amount for a Recurring Deposit (RD).

    Args:
        monthly_deposit (float): Amount deposited every month.
        annual_rate_percent (float): Annual interest rate in percent.
        years (float): Tenure in years.
        compounding_frequency (int): Compounding frequency per year (default is 4 for quarterly).

    Returns:
        dict: Contains maturity amount, total investment, and interest earned.
    """
    r = annual_rate_percent / 100
    n = compounding_frequency
    t = years
    months = int(t * 12)

    # Effective interest rate per compounding period
    rate_per_period = r / n

    # Approximation: Treat each monthly deposit as a separate compound interest series
    maturity_amount = 0
    for i in range(months):
        time_remaining = (months - i) / 12  # years
        maturity_amount += monthly_deposit * (1 + rate_per_period) ** (n * time_remaining)

    total_investment = monthly_deposit * months
    interest_earned = maturity_amount - total_investment

    return {
        "maturity_amount": round(maturity_amount, 2),
        "total_investment": round(total_investment, 2),
        "interest_earned": round(interest_earned, 2)
    }

if __name__ == "__main__":
    # Example usage
    result = calculate_rd(monthly_deposit=5000, annual_rate_percent=7, years=5)

    print("RD Calculator Example")
    print("---------------------")
    print(f"Maturity Amount   : ₹{result['maturity_amount']}")
    print(f"Total Investment  : ₹{result['total_investment']}")
    print(f"Interest Earned   : ₹{result['interest_earned']}")
