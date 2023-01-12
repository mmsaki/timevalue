"""Test the annuity module."""

def test_present_value_annuity(annuity_fixture):
    """Test the present value of an annuity.
    pva = c * ((1 - (1 + i) ** -n)/ i)
    """
    expected = 1000 * ((1 - (1 + 0.06) ** -3) / 0.06)  # Actual 2673.01
    actual = annuity_fixture.present_value_of_annuity()
    assert round(actual, 2) == round(expected, 2)


def test_present_value_annuity_due(annuity_fixture):
    """Test the present value of an annuity due.
    pvad = c * ((1 - (1 + i) ** -n)/ i) * (1 + i)
    """
    expected = 1000 * ((1 - (1 + 0.06) ** -3) / 0.06) * \
        (1 + 0.06)  # Actual 2833.39
    actual = annuity_fixture.present_value_of_annuity_due()
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_annuity(annuity_growth_fixture):
    """Test the present value of a growing annuity.
    pvifga c / (r - gr) * (1 - ((1+gr)/(1+r))**t)"""
    expected = 1000 / (0.06 - 0.10) * (1 - ((1 + 0.10) / (1 + 0.06)) ** 3)
    # Actual 2938.33
    actual = annuity_growth_fixture.present_value_of_growing_annuity()
    assert round(actual, 2) == round(expected, 2)


def test_present_value_of_growing_annuity_due(annuity_growth_fixture):
    """Test the present value of a growing annuity due.
    pvad = c * (1 + i) * (1 - (1 + g) **n * (1 + i) ** -n) / (i - g)
    """
    expected = (
        1000 * (1 + 0.06) * (1 - (1 + 0.10) ** 3 *
                             (1 + 0.06) ** -3) / (0.06 - 0.10)
    )
    # Actual 3114.63
    actual = annuity_growth_fixture.present_value_of_growing_annuity_due()
    assert round(actual, 2) == round(expected, 2)


def test_future_value_annuity(annuity_fixture):
    """Test the future value of an annuity.
    fva = c * ((1 + r) ** t - 1) / r
    """
    expected = 1000 * ((1 + 0.06) ** 3 - 1) / 0.06
    # Actual 3183.60
    actual = annuity_fixture.future_value_of_annuity()
    assert round(actual, 2) == round(expected, 2)


def test_future_value_annuity_due(annuity_fixture):
    """Test the future value of an annuity due.
    fvad = c * ((1 + r) ** t - 1) / r * (1 + r)
    """
    expected = 1000 * ((1 + 0.06) ** 3 - 1) / 0.06 * (1 + 0.06)
    # Actual 3374.62
    actual = annuity_fixture.future_value_of_annuity_due()
    assert round(actual, 2) == round(expected, 2)


def test_future_value_of_growning_annuity(annuity_growth_fixture):
    """Test the future value of a growing annuity.
    fva = c * ((1+r)**t - (1+gr)**t) / (r - gr)
    """
    expected = 1000 * ((1 + 0.06) ** 3 - (1 + 0.10) ** 3) / (0.06 - 0.10)
    # Actual 3499.60
    actual = annuity_growth_fixture.future_value_of_growing_annuity()
    assert round(actual, 2) == round(expected, 2)


def test_future_value_of_growning_annuity_due(annuity_growth_fixture):
    """Test the future value of a growing annuity due.
    fvad =  c * ((1+r)**t - (1+gr)**t) / (r - gr) * (1 + r)
    """
    expected = 1000 * ((1 + 0.06) ** 3 - (1 + 0.10) ** 3) / \
        (0.06 - 0.10) * (1 + 0.06)
    # Actual 3709.58
    actual = annuity_growth_fixture.future_value_of_growing_annuity_due()
    assert round(actual, 2) == round(expected, 2)
