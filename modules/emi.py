def calculate_emi(principal, annual_rate_percent, tenure_years):
    """
    Calculate EMI (Equated Monthly Installment), total payment, and interest.

    Args:
        principal (float): Loan amount.
        annual_rate_percent (float): Annual interest rate in percent.
        tenure_years (int or float): Tenure in years.

    Returns:
        dict: Contains EMI, total payment, and total interest.
    """
    r = annual_rate_percent / 12 / 100  # Monthly interest rate
    n = int(tenure_years * 12)          # Total number of EMIs

    emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
    total_payment = emi * n
    total_interest = total_payment - principal

    return {
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2)
    }

if __name__ == "__main__":
    # Example usage
    result = calculate_emi(principal=1000000, annual_rate_percent=8.5, tenure_years=20)

    print("EMI Calculator Example")
    print("----------------------")
    print(f"Monthly EMI       : ₹{result['emi']}")
    print(f"Total Payment     : ₹{result['total_payment']}")
    print(f"Total Interest    : ₹{result['total_interest']}")
