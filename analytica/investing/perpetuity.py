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
    def __init__(self):
        pass

    # Present value of perpetuity
    def present_value_of_perpetuity(self, cash_flow: int, discount_rate: int) -> float:
        """Calculate the present value of perpetuity.
        pvp = c / r
        Args:
            cash_flow (float): The cash flow of the investment.
            discount_rate (float): The discount rate of the investment.
            Returns:
                float: The present value of perpetuity.
        """
        return float(Decimal(str(cash_flow)) / Decimal(str(discount_rate)))

    # Present value of perpetuity due
    def present_value_of_perpetuity_due(
        self, cash_flow: int, interest_rate: int
    ) -> float:
        """Calculate the present value of perpetuity due.
        pvpd = c / r * (1 + r)
        Args:
            cash_flow (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            Returns:
                float: The present value of perpetuity due.
        """
        return float(
            Decimal(str(cash_flow))
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of growing perpetuity
    def present_value_of_growing_perpetuity(
        self, cash_flow: int, interest_rate: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing perpetuity.
        pvgp = c / (i - g)
        Args:
            cash_flow (float): The cash flow of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity.
        """
        return float(
            Decimal(str(cash_flow))
            / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
        )

    # Present value of growing perpetuity due
    def present_value_of_growing_perpetuity_due(
        self, cash_flow: int, interest_rate: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing perpetuity due.
        pvgpd = c * (r - gr) / ((1 + gr) * (1 + r))
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity due.
        """
        return float(
            Decimal(str(cash_flow))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / ((1 + Decimal(str(growth_rate))) * (1 + Decimal(str(interest_rate))))
        )
