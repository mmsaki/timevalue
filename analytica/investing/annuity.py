from decimal import Decimal

"""Annuity Class.

This module contains the Annuity class, which contains methods for calculating
the future value of annuity, present value of annuity, future value of annuity
due and present value of annuity due.

Definitions:
    Annuity: An annuity is a series of equal cash flows that occur at regular
        intervals.
    Annuity Due: An annuity due is an annuity that starts at the beginning of the
        period.
    IRA vs Annuity: An IRA is a retirement account that allows you to invest in
        stocks, bonds, mutual funds, and other investments. An annuity is a
        contract between you and an insurance company that pays you a fixed
        amount of money each year for the rest of your life.

References:
    https://www.investopedia.com/terms/a/annuity.asp
    https://www.investopedia.com/terms/a/annuitydue.asp
"""


class Annuity:
    def __init__(self):
        pass

    # Future value of annuity
    def future_value_of_annuity(
        self, present_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of annuity.
        fva = pva * ((1 + r) ** t - 1) / r
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of annuity.
        """
        return float(
            Decimal(str(present_value))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
        )

    # Present value of annuity
    def present_value_of_annuity(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of annuity.
        pva = c * ((1 - (1 + i) ** -n)/ i)
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of annuity.
        """
        return float(
            Decimal(str(future_value))
            * (
                (1 - (1 + Decimal(str(interest_rate))) ** -Decimal(str(time)))
                / Decimal(str(interest_rate))
            )
        )

    # Future value of annuity due
    def future_value_of_annuity_due(
        self, cash_flow: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of annuity due.
        fvad = c * ((1 + r) ** t - 1) / r * (1 + r)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of annuity due.
        """
        return float(
            Decimal(str(cash_flow))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of annuity due
    def present_value_of_annuity_due(
        self, cash_flow: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of annuity due.
        pvad = c * (1 - (1+r) ** -t) / r) * (1 + r)
        Args:
            cash_flow (float): The cash flow of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of annuity due.
        """
        return float(
            Decimal(str(cash_flow))
            * (1 - (1 + Decimal(str(interest_rate))) ** -Decimal(str(time)))
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Future value of growing annuity
    def future_value_of_growing_annuity(
        self, cash: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the future value of growing annuity.
        fvga = c * ((1+r)**t - (1+gr)**t) / (r - gr)
        Args:
            cash (float): The cash value of the first payment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of growing annuity.
        """
        return float(
            Decimal(str(cash))
            * (
                (1 + Decimal(str(interest_rate))) ** Decimal(str(time))
                - (1 + Decimal(str(growth_rate))) ** Decimal(str(time))
            )
            / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
        )

    # Present value of growing annuity
    def present_value_of_growing_annuity(
        self, first_payment: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing annuity.
        pvga = p / (r - gr) * (1- ((1+gr)/(1+r))**t)
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing annuity.
        """
        return float(
            Decimal(str(first_payment))
            / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            * (
                1 - ((1 + Decimal(str(growth_rate))) / (1 + Decimal(str(interest_rate))))
                ** Decimal(str(time))
            )
        )

    # Future value of growing annuity due
    def future_value_of_growing_annuity_due(
        self, present_value: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the future value of growing annuity due.
        fvgad = pva * ((1 + gr) / (r - gr)) * ((1 + r) ** t - 1) * (1 + r)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of growing annuity due.
        """
        return float(
            Decimal(str(present_value))
            * (
                (1 + Decimal(str(growth_rate)))
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of growing annuity due
    def present_value_of_growing_annuity_due(
        self, future_value: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing annuity due.
        pvgad = fv * (r - gr) / ((1 + gr) * ((1 + r) ** t - 1) * (1 + r))
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing annuity due.
        """
        return float(
            Decimal(str(future_value))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / (
                (1 + Decimal(str(growth_rate)))
                * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
                * (1 + Decimal(str(interest_rate)))
            )
        )

    # Future value of ordinary annuity
    def future_value_of_ordinary_annuity(
        self, present_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of ordinary annuity.
        fvoa = pva * ((1 + r) ** t - 1) / r
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of ordinary annuity.
        """
        return float(
            Decimal(str(present_value))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
        )

    # Present value of ordinary annuity
    def present_value_of_ordinary_annuity(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of ordinary annuity.
        pvoad = fv * r / ((1 + r) ** t - 1)
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of ordinary annuity.
        """
        return float(
            Decimal(str(future_value))
            * Decimal(str(interest_rate))
            / ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
        )

    # Future value of ordinary annuity due
    def future_value_of_ordinary_annuity_due(
        self, present_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of ordinary annuity due.
        fvoad = pva * ((1 + r) ** t - 1) / r * (1 + r)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of ordinary annuity due.
        """
        return float(
            Decimal(str(present_value))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of ordinary annuity due
    def present_value_of_ordinary_annuity_due(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of ordinary annuity due.
        pvoad = fv * r / ((1 + r) ** t - 1) * (1 + r)
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of ordinary annuity due.
        """
        return float(
            Decimal(str(future_value))
            * Decimal(str(interest_rate))
            / ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            * (1 + Decimal(str(interest_rate)))
        )

    # Future value of growing ordinary annuity
    def future_value_of_growing_ordinary_annuity(
        self, present_value: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the future value of growing ordinary annuity.
        fvgoad = pva * ((1 + r) ** t - 1) / (r - gr) * (1 + gr)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of growing ordinary annuity.
        """
        return float(
            Decimal(str(present_value))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            * (1 + Decimal(str(growth_rate)))
        )

    # Present value of growing ordinary annuity
    def present_value_of_growing_ordinary_annuity(
        self, future_value: int, interest_rate: int, time: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing ordinary annuity.
        pvgoad = fv * (r - gr) / ((1 + r) ** t - 1) * (1 + gr)
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing ordinary annuity.
        """
        return float(
            Decimal(str(future_value))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            * (1 + Decimal(str(growth_rate)))
        )
