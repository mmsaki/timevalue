from decimal import Decimal

"""Perpetuity Class.

This module contains the Perpetuity class, which contains methods for
calculating the present value of perpetuity, present value of perpetuity due and
present value of growing perpetuity.


Definitions:
    Perpetuity: A perpetuity is an annuity that never ends.
    Perpetuity Due: A perpetuity due is a perpetuity that starts at the beginning
        of the period.
    Growing Perpetuity: A growing perpetuity is a perpetuity that grows at a
        constant rate.

References:
    https://www.investopedia.com/terms/p/perpetuity.asp
    https://www.investopedia.com/terms/p/perpetuitydue.asp
    https://www.investopedia.com/terms/p/growingperpetuity.asp
"""


class Perpetuity:
    def __init__(self, cash_flow: float, discount_rate: float):
        self.cash_flow = Decimal(str(cash_flow))
        self.discount_rate = Decimal(str(discount_rate))

    # Present value of perpetuity
    def present_value_of_perpetuity(self) -> float:
        """Calculate the present value of perpetuity.
        pvp = c / r
        Args:
            cash_flow (float): The cash flow of the investment.
            discount_rate (float): The discount rate of the investment.
            Returns:
                float: The present value of perpetuity.
        """
        return float(self.cash_flow / self.discount_rate)

    # Present value of perpetuity due
    def present_value_of_perpetuity_due(self) -> float:
        """Calculate the present value of perpetuity due.
        pvpd = c / r * (1 + r)
        Args:
            cash_flow (float): The future value of the investment.
            discount_rate (float): The interest rate of the investment.
            Returns:
                float: The present value of perpetuity due.
        """
        return float(self.cash_flow / self.discount_rate * (1 + self.discount_rate))


class GrowingPerpetuity:
    def __init__(self, cash_flow: float, discount_rate: float, growth_rate: float):
        self.cash_flow = Decimal(str(cash_flow))
        self.discount_rate = Decimal(str(discount_rate))
        self.growth_rate = Decimal(str(growth_rate))

    # Present value of growing perpetuity
    def present_value_of_growing_perpetuity(self) -> float:
        """Calculate the present value of growing perpetuity.
        pvgp = c / (i - g)
        Args:
            cash_flow (float): The cash flow of the investment.
            discount_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity.
        """
        return float(self.cash_flow / (self.discount_rate - self.growth_rate))

    # Present value of growing perpetuity due
    def present_value_of_growing_perpetuity_due(self) -> float:
        """Calculate the present value of growing perpetuity due.
        pvgpd = c * (r - gr) / ((1 + gr) * (1 + r))
        Args:
            future_value (float): The future value of the investment.
            discount_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity due.
        """
        return float(
            self.cash_flow
            * (self.discount_rate - self.growth_rate)
            / ((1 + self.growth_rate) * (1 + self.discount_rate))
        )
