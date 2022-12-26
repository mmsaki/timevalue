# analytica

Analytica is a simple Python package for analytics and investing tools

To install use `pip install analytica`

Use analytica anywhere outside of your project.

```bash
analytica <present_value> <interest_rate> <time>
```

## Using import within python projects

```python3
from analytica.investing import money

initialize = money.Calculate()
initialize.future_value_of_money(present_value, interest_rate, time)
```