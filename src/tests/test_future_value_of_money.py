import pytest

from investing import time_value_money


def test_future_value_of_money():
    """Test the future value of money."""
    # Arrange
    present_value = 100
    interest_rate = 0.05
    time = 5
    expected = 127.628
    # Act
    actual = time_value_money.TVM().future_value_of_money(
        present_value, interest_rate, time
    )
    # Assert
    assert round(actual, 3) == expected


def test_present_value_of_money():
    """Test the present value of money."""
    # Arrange
    future_value = 100
    interest_rate = 0.05
    time = 5
    expected = 78.353
    # Act
    actual = time_value_money.TVM().present_value_of_money(
        future_value, interest_rate, time
    )
    # Assert
    assert round(actual, 3) == expected
