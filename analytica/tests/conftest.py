import pytest

from analytica.investing import annuity, perpetuity, time_value_money


@pytest.fixture(scope="module")
def time_value_money_fixture():
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    return time_value_money.TimeValueOfMoney(cash_flow, interest_rate, time)


@pytest.fixture(scope="module")
def annuity_fixture():
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    return annuity.Annuity(cash_flow, interest_rate, time)


@pytest.fixture(scope="module")
def annuity_growth_fixture():
    cash_flow = 1000
    interest_rate = 0.06
    time = 3
    growth_rate = 0.10
    return annuity.GrowingAnnuity(cash_flow, interest_rate, growth_rate, time)


@pytest.fixture(scope="module")
def perpetuity_fixture():
    cash_flow = 1000
    discount_rate = 0.06
    return perpetuity.Perpetuity(cash_flow, discount_rate)


@pytest.fixture(scope="module")
def perpetuity_growth_fixture():
    cash_flow = 1000
    discount_rate = 0.06
    growth_rate = 0.10
    return perpetuity.GrowingPerpetuity(cash_flow, discount_rate, growth_rate)
