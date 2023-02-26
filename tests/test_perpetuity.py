def test_present_value_of_perpetuity(perpetuity_fixture):
    """Test the future value of perpetuity.
    pv = c / r
    """
    expected = 1000 / 0.06
    actual = perpetuity_fixture.present_value_of_perpetuity()
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_perpetuity_due(perpetuity_fixture):
    """Test the future value of perpetuity.
    pv = c / r * (1 + r)
    """
    expected = 1000 / 0.06 * (1 + 0.06)
    actual = perpetuity_fixture.present_value_of_perpetuity_due()
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_perpetuity(perpetuity_growth_fixture):
    """Test the future value of growing perpetuity.
    pv = c / (r - gr)
    """
    expected = 1000 / (0.06 - 0.10)
    actual = perpetuity_growth_fixture.present_value_of_growing_perpetuity()
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_perpetuity_due(perpetuity_growth_fixture):
    """Test the future value of growing perpetuity due.
    pv = c * (r - gr) / ((1 + gr) * (1 + r))
    """
    expected = 1000 * (0.06 - 0.10) / ((1 + 0.10) * (1 + 0.06))
    actual = perpetuity_growth_fixture.present_value_of_growing_perpetuity_due()
    # Assert
    assert round(actual, 2) == round(expected, 2)
