from analytica.investing import time_value_money


def test_future_value_of_money():
    """Test the future value of money."""
    # Arrange
    present_value = 100
    interest_rate = 0.05
    time = 5
    expected = 127.63
    # Act
    actual = time_value_money.TimeValueOfMoney().future_value_of_money(
        present_value, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == expected


def test_present_value_of_money():
    """Test the present value of money."""
    # Arrange
    future_value = 100
    interest_rate = 0.05
    time = 5
    expected = 78.35
    # Act
    actual = time_value_money.TimeValueOfMoney().present_value_of_money(
        future_value, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == expected
