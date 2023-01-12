from analytica.investing import time_value_money


def test_present_value_of_money(time_value_money_fixture):
    """Test the present value of money."""
    # pv = fv / (1 + r) ** t
    expected = 1000 / (1 + 0.06) ** 3
    actual = time_value_money_fixture.present_value_of_money()
    assert round(actual, 2) == round(expected, 2)


def test_future_value_of_money(time_value_money_fixture):
    """Test the future value of money."""
    # fv = pv * (1 + r) ** t
    expected = 1000 * (1 + 0.06) ** 3
    actual = time_value_money_fixture.future_value_of_money()
    assert round(actual, 2) == round(expected, 2)
