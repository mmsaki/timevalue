from decimal import Decimal


class TimeValueOfMoney:
    def __init__(self, cash_flow: float, interest_rate: float, time: int):
        self.cash_flow = Decimal(str(cash_flow))
        self.interest_rate = Decimal(str(interest_rate))
        self.time = Decimal(str(time))

    # Present value of money
    def present_value_of_money(self) -> float:
        """Calculate the present value of money.
        pv = fv / (1 + r) ** t
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of money.
        """
        return float(self.cash_flow / (1 + self.interest_rate) ** self.time)

    # Future value of money
    def future_value_of_money(self) -> float:
        """Calculate the future value of money.
        fv = pv * (1 + r) ** t
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of money.
        """
        return float(self.cash_flow * (1 + self.interest_rate) ** self.time)
