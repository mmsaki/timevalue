import pytest

from analytica.investing import perpetuity


def test_present_value_of_perpetuity():
    """Test the future value of perpetuity.
    pv = c / r
    """
    # Arrange
    cash_flow = 2
    discount_rate = 0.05
    expected = 2 / 0.05
    # Actual
    actual = perpetuity.Perpetuity().present_value_of_perpetuity(
        cash_flow, discount_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)
