from decimal import Decimal

"""Annuity Class.

This module contains the Annuity class, which contains methods for calculating
the future value of annuity, present value of annuity, future value of annuity
due and present value of annuity due.

Definitions:
    Annuity: A series of equal payments or receipts occurring over a specified 
        number of periods. In an ordinary annuity, payments or receipts occur at 
        the end of each period; in an annuity due, payments or receipts occur at 
        the beginning of each period.
    Growing Annuity: A series of payments or receipts occurring over a specified 
        number of periods that increase each period at a constant percentage. 
        In a growing ordinary annuity, payments or receipts occur at the end of 
        each period; in a growing annuity due, payments or receipts occur at the 
        beginning of each period.
References:
    https://www.investopedia.com/terms/a/annuity.asp
    https://www.investopedia.com/terms/a/annuitydue.asp
"""


class Annuity:
    def __init__(self):
        pass

    def present_value_of_annuity(
        self, future_value: int, interest_rate: int, time: int, pv: bool = False
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
        rate = (1 - (1 + Decimal(str(interest_rate))) ** -Decimal(str(time))) / Decimal(
            str(interest_rate)
        )
        if not pv:
            return float(Decimal(str(future_value)) * rate)
        else:
            return float(Decimal(str(future_value)) / rate)

    def present_value_of_annuity_due(
        self, cash_flow: int, interest_rate: int, time: int, pv: bool = False
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
        rate = (
            (1 - (1 + Decimal(str(interest_rate))) ** -Decimal(str(time)))
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )
        if not pv:
            return float(Decimal(str(cash_flow)) * rate)
        else:
            return float(Decimal(str(cash_flow)) / rate)

    def present_value_of_growing_annuity(
        self,
        cash_flow: int,
        interest_rate: int,
        time: int,
        growth_rate: int,
        pv: bool = False,
    ) -> float:
        """Calculate the present value of growing annuity.
        pvga = c  * (1 - ((1+gr)/(1+r))**t) / (r - gr)
        Args:
            cash_flow (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing annuity.
        """
        if interest_rate == growth_rate:
            # pv = c * n/(1+i)
            rate = Decimal(str(time)) / (1 + Decimal(str(interest_rate)))
            if not pv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)
        else:
            rate = (
                1
                - ((1 + Decimal(str(growth_rate))) / (1 + Decimal(str(interest_rate))))
                ** Decimal(str(time))
            ) / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            if not pv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)

    def present_value_of_growing_annuity_due(
        self,
        cash_flow: int,
        interest_rate: int,
        time: int,
        growth_rate: int,
        pv: bool = False,
    ) -> float:
        """Calculate the present value of growing annuity due.
        pvgad = c * (1 + i) * (1 - (1 + gr)**t * (1 + i)**-t) / (i - gr)
        Args:
            cash_flow (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing annuity due.
        """
        if interest_rate == growth_rate:
            # pv = c * n/(1+i) * (1 + i)
            rate = (
                Decimal(str(time))
                / (1 + Decimal(str(interest_rate)))
                * (1 + Decimal(str(interest_rate)))
            )
            if not pv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)
        else:
            rate = (
                (1 + Decimal(str(interest_rate)))
                * (
                    1
                    - (1 + Decimal(str(growth_rate))) ** Decimal(str(time))
                    * (1 + Decimal(str(interest_rate))) ** -Decimal(str(time))
                )
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
            if not pv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)

    def future_value_of_annuity(
        self, cash_flow: int, interest_rate: int, time: int, fv: bool = False
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
        rate = ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1) / Decimal(
            str(interest_rate)
        )
        if not fv:
            return float(Decimal(str(cash_flow)) * rate)
        else:
            return float(Decimal(str(cash_flow)) / rate)

    def future_value_of_annuity_due(
        self, cash_flow: int, interest_rate: int, time: int, fv: bool = False
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
        rate = (
            ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )
        if not fv:
            return float(Decimal(str(cash_flow)) * rate)
        else:
            return float(Decimal(str(cash_flow)) / rate)

    def future_value_of_growing_annuity(
        self,
        cash_flow: int,
        interest_rate: int,
        time: int,
        growth_rate: int,
        fv: bool = False,
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
        if interest_rate == growth_rate:
            # fv = c * (1+i)** (t-1)
            rate = Decimal(str(time)) * (1 + Decimal(str(interest_rate))) ** (
                Decimal(str(time)) - 1
            )
            if not fv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)
        else:
            rate = (
                (1 + Decimal(str(interest_rate))) ** Decimal(str(time))
                - (1 + Decimal(str(growth_rate))) ** Decimal(str(time))
            ) / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            if not fv:
                return float(Decimal(str(cash_flow)) * rate)
            else:
                return float(Decimal(str(cash_flow)) / rate)

    def future_value_of_growing_annuity_due(
        self,
        present_value: int,
        interest_rate: int,
        time: int,
        growth_rate: int,
        fv: bool = False,
    ) -> float:
        """Calculate the future value of growing annuity due.
        fvgad = c * ((1+r)**t - (1+gr)**t) / (r - gr) * (1+r)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of growing annuity due.
        """
        if interest_rate == growth_rate:
            # fv = c * (1+i)** (t)
            rate = Decimal(str(time)) * (1 + Decimal(str(interest_rate))) ** (
                Decimal(str(time))
            )
            if not fv:
                return float(Decimal(str(present_value)) * rate)
            else:
                return float(Decimal(str(present_value)) / rate)
        else:
            rate = (
                (1 + Decimal(str(interest_rate)))
                * (
                    (1 + Decimal(str(interest_rate))) ** Decimal(str(time))
                    - (1 + Decimal(str(growth_rate))) ** Decimal(str(time))
                )
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
            if not fv:
                return float(Decimal(str(present_value)) * rate)
            else:
                return float(Decimal(str(present_value)) / rate)
