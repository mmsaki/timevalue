import pytest

from analytica.investing import money


def test_present_value_annuity_due():
    """Test the present value of an annuity due.
    pvad = c * ((1 - (1 + i) ** -n)/ i) * (1 + i)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.05
    time = 5
    expected = 1000 * ((1 - (1 + 0.05) ** -5) / 0.05) * (1 + 0.05)
    # Actual
    actual = money.Annuity().present_value_of_annuity_due(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_future_value_annuity_due():
    """Test the future value of an annuity due.
    fvad = c * ((1 + r) ** t - 1) / r * (1 + r)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.05
    time = 5
    expected = 1000 * ((1 + 0.05) ** 5 - 1) / 0.05 * (1 + 0.05)
    # Actual
    actual = money.Annuity().future_value_of_annuity_due(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_annuity():
    """Test the present value of an annuity.
    pva = c * ((1 - (1 + i) ** -n)/ i)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.05
    time = 5
    expected = 1000 * ((1 - (1 + 0.05) ** -5) / 0.05)
    # Actual
    actual = money.Annuity().present_value_of_annuity(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_future_value_annuity():
    """Test the future value of an annuity.
    fva = c * ((1 + r) ** t - 1) / r
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.05
    time = 5
    expected = 1000 * ((1 + 0.05) ** 5 - 1) / 0.05
    # Actual
    actual = money.Annuity().future_value_of_annuity(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)
