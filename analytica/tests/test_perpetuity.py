from analytica.investing import perpetuity


def test_present_value_of_perpetuity():
    """Test the future value of perpetuity.
    pv = c / r
    """
    # Arrange
    cash_flow = 500
    discount_rate = 0.04
    expected = 500 / 0.04
    # Actual
    actual = perpetuity.Perpetuity().present_value_of_perpetuity(
        cash_flow, discount_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_perpetuity_due():
    """Test the future value of perpetuity.
    pv = c / r * (1 + r)
    """
    # Arrange
    cash_flow = 500
    discount_rate = 0.04
    expected = 500 / 0.04 * (1 + 0.04)
    # Actual
    actual = perpetuity.Perpetuity().present_value_of_perpetuity_due(
        cash_flow, discount_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)
