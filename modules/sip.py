def calculate_sip(monthly_investment, annual_rate_percent, years):
    """
    Calculate the future value of a Systematic Investment Plan (SIP).

    Args:
        monthly_investment (float): Amount invested every month.
        annual_rate_percent (float): Annual return rate in percent (e.g., 12 for 12%).
        years (int or float): Investment duration in years.

    Returns:
        dict: Contains future value, total investment, and wealth gained.
    """
    r = annual_rate_percent / 12 / 100  # Monthly interest rate
    n = int(years * 12)                 # Total number of payments
    fv = monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)

    total_investment = monthly_investment * n
    wealth_gain = fv - total_investment

    return {
        "future_value": round(fv, 2),
        "total_investment": round(total_investment, 2),
        "wealth_gain": round(wealth_gain, 2)
    }

if __name__ == "__main__":
    # Example usage when running this file directly
    example = calculate_sip(monthly_investment=5000, annual_rate_percent=12, years=10)

    print("SIP Calculator Example")
    print("----------------------")
    print(f"Future Value     : ₹{example['future_value']}")
    print(f"Total Investment : ₹{example['total_investment']}")
    print(f"Wealth Gain      : ₹{example['wealth_gain']}")
