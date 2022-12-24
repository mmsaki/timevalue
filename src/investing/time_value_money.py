from decimal import Decimal
from typing import Any, Dict, List, Tuple, Union


class TVM:
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

    # Future value of annuity
    def future_value_of_annuity(
        self, present_value: int, interest_rate: int, time: float
    ) -> float:
        """Calculate the future value of annuity.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of annuity.
        """
        return float(
            Decimal(str(present_value))
            * (
                Decimal(str(interest_rate))
                * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            )
            / Decimal(str(interest_rate))
        )

    # Present value of annuity
    def present_value_of_annuity(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of annuity.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of annuity.
        """
        return future_value * interest_rate / ((1 + interest_rate) ** time - 1)

    # Future value of annuity due
    def future_value_of_annuity_due(
        self, present_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the future value of annuity due.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of annuity due.
        """
        return float(
            Decimal(str(present_value))
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of annuity due
    def present_value_of_annuity_due(
        self, future_value: int, interest_rate: int, time: int
    ) -> float:
        """Calculate the present value of annuity due.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of annuity due.
        """
        return float(
            Decimal(str(future_value))
            * Decimal(str(interest_rate))
            / ((1 + Decimal(str(interest_rate))) ** time - 1)
            / (1 + Decimal(str(interest_rate)))
        )

    # Future value of perpetuity
    def future_value_of_perpetuity(
        self, present_value: int, interest_rate: int
    ) -> float:
        """Calculate the future value of perpetuity.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            Returns:
                float: The future value of perpetuity.
        """
        return float(Decimal(str(present_value)) / Decimal(str(interest_rate)))

    # Present value of perpetuity
    def present_value_of_perpetuity(
        self, future_value: int, interest_rate: int
    ) -> float:
        """Calculate the present value of perpetuity.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            Returns:
                float: The present value of perpetuity.
        """
        return float(Decimal(str(future_value)) * Decimal(str(interest_rate)))

    # Future value of perpetuity due
    def future_value_of_perpetuity_due(
        self, present_value: int, interest_rate: int
    ) -> float:
        """Calculate the future value of perpetuity due.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            Returns:
                float: The future value of perpetuity due.
        """
        return float(
            Decimal(str(present_value))
            / Decimal(str(interest_rate))
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of perpetuity due
    def present_value_of_perpetuity_due(
        self, future_value: int, interest_rate: int
    ) -> float:
        """Calculate the present value of perpetuity due.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            Returns:
                float: The present value of perpetuity due.
        """
        return float(
            Decimal(str(future_value))
            * Decimal(str(interest_rate))
            / (1 + Decimal(str(interest_rate)))
        )

    # Future value of growing annuity
    def future_value_of_growing_annuity(
        self, present_value: int, interest_rate: int, growth_rate: int, time: int
    ) -> float:
        """Calculate the future value of growing annuity.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The future value of growing annuity.
        """
        return float(
            Decimal(str(present_value))
            * (
                (1 + Decimal(str(growth_rate)))
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
            * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
        )

    # Present value of growing annuity
    def present_value_of_growing_annuity(
        self, future_value: int, interest_rate: int, growth_rate: int, time: int
    ) -> float:
        """Calculate the present value of growing annuity.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            time (int): The time period of the investment.
            Returns:
                float: The present value of growing annuity.
        """
        return float(
            Decimal(str(future_value))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / (
                (1 + Decimal(str(growth_rate)))
                * ((1 + Decimal(str(interest_rate))) ** Decimal(str(time)) - 1)
            )
        )

    # Future value of growing annuity due
    def future_value_of_growing_annuity_due(
        self, present_value: int, interest_rate: int, growth_rate: int, time: int
    ) -> float:
        """Calculate the future value of growing annuity due.
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
        self, future_value: int, interest_rate: int, growth_rate: int, time: int
    ) -> float:
        """Calculate the present value of growing annuity due.
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

    # Future value of growing perpetuity
    def future_value_of_growing_perpetuity(
        self, present_value: int, interest_rate: int, growth_rate: int
    ):
        """Calculate the future value of growing perpetuity.
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The future value of growing perpetuity.
        """
        return float(
            Decimal(str(present_value))
            * (
                (1 + Decimal(str(growth_rate)))
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
        )

    # Present value of growing perpetuity
    def present_value_of_growing_perpetuity(
        self, future_value: int, interest_rate: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing perpetuity.
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity.
        """
        return float(
            Decimal(str(future_value))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / ((1 + Decimal(str(growth_rate))))
        )
