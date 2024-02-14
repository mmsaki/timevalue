# Timevalue

Timevalue is a simple Python package for finding the time value of money

```bash
pip install timevalue
```

## Run Tests

To run tests:

```bash
pytest --verbosity=1
```

## Future & Present Cli Commands

Find future value of money for $1000$ at $0.03%$ interest for $2$ periods:

```bash
future 1000 .03 2 #returns 1060.90
```

Find present value of money for $1000$ at $0.03%$ interest for $2$ periods:

```bash
present 1000 .03 2 #returns 942.60
```

## Annuity Cli Command

Annuities are payments are that are paid to you as a steady stream of income. Heres an example annuity.

Q1. Find the future value of an annuity cash flow of $1000$ with and interest rate of $0.06$ for $3$ periods.

```bash
annuity --future_value --cash_flow 1000 --interest_rate 0.06 --time 3 # returns 2673.011949461636
```

Say we want calculate the annuity present value given the cash flow as the result from Q1, use the `--present_value` and `--pv` flag to get the cash flow value:

```bash
annuity --present_value --cash_flow 2673.011949461636 --interest_rate 0.06 --time 3 --pv
```

Heres an example of growing annuity due.

```bash
annuity --future_value --due --cash_flow 1000 --interest_rate 0.06 --time 3 --growth_rate .10
```

Output:

```bash
3709.576
```

You can access the help by using `annuity --help`.

## Import timevalue package

```python3
In [1]: from timevalue.investing import time_value_money

In [2]: initialize = time_value_money.TimeValueOfMoney()

In [3]: initialize.future_value_of_money(1000, .03, 2)
Out[3]: 1060.9

In [4]: initialize.present_value_of_money(1000, .03, 2)
Out[4]: 942.5959091337544
```

See more [examples](https://github.com/mmsaki/timevalue/blob/main/src/timevalue/examples/annuities.md).
