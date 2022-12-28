from decimal import Decimal


class TimeValueOfMoney:
    def __init__(self):
        pass

    def calculate(self, a: int, b: int) -> float:
        """Calculate accurate value of money floats."""
        return float(Decimal(str(a)) + Decimal(str(b)))

    # Future value of money
    def future_value_of_money(
        self, present_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of money.
        fv = pv * (1 + r) ** t
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of money.
        """
        return float(
            Decimal(str(present_value))
            * (1 + Decimal(str(interest_rate))) ** Decimal(str(time))
        )

    # Present value of money
    def present_value_of_money(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of money.
        pv = fv / (1 + r) ** t
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of money.
        """
        return float(
            Decimal(str(future_value))
            / (1 + Decimal(str(interest_rate))) ** Decimal(str(time))
        )
