class Investing:
    def __init__(self):
        pass
    # Time value of money
    def time_value_of_money(self, present_value, future_value, time):
        """Calculate the time value of money.
        Args:
            present_value (float): The present value of the investment.
            future_value (float): The future value of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The time value of money.
        """
        return future_value / (present_value * (1 + time) ** time)