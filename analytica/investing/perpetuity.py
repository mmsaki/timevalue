from decimal import Decimal


class Perpetuity:
    def __init__(self):
        pass

    # Future value of perpetuity
    def future_value_of_perpetuity(
        self, present_value: int, interest_rate: int
    ) -> float:
        """Calculate the future value of perpetuity.
        fvp = pva / r
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
        pvp = fv * r
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
        fvpd = pva / (r - 1)
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
        pvpd = fv * r / (1 + r)
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

    # Future value of growing perpetuity
    def future_value_of_growing_perpetuity(
        self, present_value: int, interest_rate: int, growth_rate: int
    ):
        """Calculate the future value of growing perpetuity.
        fvgp = pva * ((1 + gr) / (r - gr))
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
        pvgp = fv * (r - gr) / (1 + gr)
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

    # Future value of growing perpetuity due
    def future_value_of_growing_perpetuity_due(
        self, present_value: int, interest_rate: int, growth_rate: int
    ) -> float:
        """Calculate the future value of growing perpetuity due.
        fvgpd = pva * ((1 + gr) / (r - gr)) * (1 + r)
        Args:
            present_value (float): The present value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The future value of growing perpetuity due.
        """
        return float(
            Decimal(str(present_value))
            * (
                (1 + Decimal(str(growth_rate)))
                / (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            )
            * (1 + Decimal(str(interest_rate)))
        )

    # Present value of growing perpetuity due
    def present_value_of_growing_perpetuity_due(
        self, future_value: int, interest_rate: int, growth_rate: int
    ) -> float:
        """Calculate the present value of growing perpetuity due.
        pvgpd = fv * (r - gr) / ((1 + gr) * (1 + r))
        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The interest rate of the investment.
            growth_rate (float): The growth rate of the investment.
            Returns:
                float: The present value of growing perpetuity due.
        """
        return float(
            Decimal(str(future_value))
            * (Decimal(str(interest_rate)) - Decimal(str(growth_rate)))
            / ((1 + Decimal(str(growth_rate))) * (1 + Decimal(str(interest_rate))))
        )
