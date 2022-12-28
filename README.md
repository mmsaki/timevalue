# analytica

Analytica is a simple Python package for analytics and investing tools

Before using the tool create a virtual envirinment

```bash
python -m venv
```

Notice that a venv directory is created in the project folder. To activate the virtual environemnt run

```bash
source ./venv/bin/activate
```

Next, install package using

```bash
python -m pip install .
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
