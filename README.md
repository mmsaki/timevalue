# analytica

Analytica is a simple Python package for analytics and investing tools

Before using the tool create a virtual environment

```bash
python -m venv venv
```

Notice that a `/venv` directory is created in the project folder. To activate the virtual environemnt run

```bash
source ./venv/bin/activate
```

Next, install package using

```bash
python -m pip install -e .
```

Use analytica in your command line interface / Terminal.

```bash
analytica 1000, .03, 2 #returns 1060.90

```

## Using import within python projects

```python3
In [1]: from analytica.investing import time_value_money

In [2]: initialize = time_value_money.TimeValueOfMoney()

In [3]: initialize.future_value_of_money(1000, .03, 2)
Out[3]: 1060.9

In [4]: initialize.present_value_of_money(1000, .03, 2)
Out[4]: 942.5959091337544
```

## Calculating annuinty value

Annuity are payments are that are paid to you as a steady stream of income. Heres an example of growing annuity due.

```bash
annuity --future_value --due --cash_flow 1000 --interest_rate 0.06 --time 3 --growth_rate .10
```

Output:

```bash
3709.576
```

You can access the help by using `annuity --help`.

```bash
usage: annuity [-h] [-c] [-p | -f] -i  -t  [-d] [-g] [--pv | --fv]

Calculate annuity payments.

options:
  -h, --help            show this help message and exit
  -c , --cash_flow      cash flow
  -p, --present_value   present value
  -f, --future_value    future value
  -i , --interest_rate  interest rate
  -t , --time           time
  -d, --due             With an annuity due, payments are made at the beginning of each period
  -g , --growth_rate    growth rate
  --pv                  reverse calculate the present value (bool)
  --fv                  reverse calculate the future value (bool)
```

See more [examples](/analytica/examples/annuities.md).
