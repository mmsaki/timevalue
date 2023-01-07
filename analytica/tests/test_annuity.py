from analytica.investing import annuity


def test_present_value_annuity():
    """Test the present value of an annuity.
    pva = c * ((1 - (1 + i) ** -n)/ i)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.05
    time = 5
    expected = 1000 * ((1 - (1 + 0.05) ** -5) / 0.05)
    # Actual 2673.01
    actual = annuity.Annuity().present_value_of_annuity(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_annuity_due():
    """Test the present value of an annuity due.
    pvad = c * ((1 - (1 + i) ** -n)/ i) * (1 + i)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    expected = 1000 * ((1 - (1 + 0.06) ** -3) / 0.06) * (1 + 0.06)
    # Actual 2833.39
    actual = annuity.Annuity().present_value_of_annuity_due(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_annuity():
    """Test the present value of a growing annuity.
    pvifga c / (r - gr) * (1 - ((1+gr)/(1+r))**t)"""
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    growth_rate = 0.10
    expected = 1000 / (0.06 - 0.10) * (1 - ((1 + 0.10) / (1 + 0.06)) ** 3)
    # Actual 2938.33
    actual = annuity.Annuity().present_value_of_growing_annuity(
        cash_flow, interest_rate, time, growth_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_annuity_due():
    """Test the present value of a growing annuity due.
    pvad = c * (1 + i) * (1 - (1 + g) **n * (1 + i) ** -n) / (i - g)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    growth_rate = 0.10
    expected = (
        1000 * (1 + 0.06) * (1 - (1 + 0.10) ** 3 * (1 + 0.06) ** -3) / (0.06 - 0.10)
    )
    # Actual 3114.63
    actual = annuity.Annuity().present_value_of_growing_annuity_due(
        cash_flow, interest_rate, time, growth_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_future_value_annuity():
    """Test the future value of an annuity.
    fva = c * ((1 + r) ** t - 1) / r
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    expected = 1000 * ((1 + 0.06) ** 3 - 1) / 0.06
    # Actual 3183.60
    actual = annuity.Annuity().future_value_of_annuity(
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
    interest_rate = 0.06
    time = 3
    expected = 1000 * ((1 + 0.06) ** 3 - 1) / 0.06 * (1 + 0.06)
    # Actual 3374.62
    actual = annuity.Annuity().future_value_of_annuity_due(
        cash_flow, interest_rate, time  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_future_value_of_growning_annuity():
    """Test the future value of a growing annuity.
    fva = c * ((1+r)**t - (1+gr)**t) / (r - gr)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    growth_rate = 0.10
    expected = 1000 * ((1 + 0.06) ** 3 - (1 + 0.10) ** 3) / (0.06 - 0.10)
    # Actual 3499.60
    actual = annuity.Annuity().future_value_of_growing_annuity(
        cash_flow, interest_rate, time, growth_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)


def test_future_value_of_growning_annuity_due():
    """Test the future value of a growing annuity due.
    fvad =  c * ((1+r)**t - (1+gr)**t) / (r - gr) * (1 + r)
    """
    # Arrange
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    growth_rate = 0.10
    expected = 1000 * ((1 + 0.06) ** 3 - (1 + 0.10) ** 3) / (0.06 - 0.10) * (1 + 0.06)
    # Actual 3709.58
    actual = annuity.Annuity().future_value_of_growing_annuity_due(
        cash_flow, interest_rate, time, growth_rate  # type: ignore
    )
    # Assert
    assert round(actual, 2) == round(expected, 2)
