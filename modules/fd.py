def calculate_fd(principal, annual_rate_percent, years, compounding_frequency=4):
    """
    Calculate the maturity amount for a fixed deposit using compound interest.

    Args:
        principal (float): Initial deposit amount.
        annual_rate_percent (float): Annual interest rate in percent.
        years (float): Deposit duration in years.
        compounding_frequency (int): Compounding per year (default is 4 for quarterly).

    Returns:
        dict: Contains maturity amount and interest earned.
    """
    r = annual_rate_percent / 100
    n = compounding_frequency
    t = years

    maturity_amount = principal * (1 + r / n) ** (n * t)
    interest_earned = maturity_amount - principal

    return {
        "maturity_amount": round(maturity_amount, 2),
        "interest_earned": round(interest_earned, 2)
    }

if __name__ == "__main__":
    # Example usage
    result = calculate_fd(principal=100000, annual_rate_percent=7, years=5, compounding_frequency=4)

    print("FD Calculator Example")
    print("---------------------")
    print(f"Maturity Amount  : ₹{result['maturity_amount']}")
    print(f"Interest Earned  : ₹{result['interest_earned']}")
