import sys
from decimal import Decimal

from analytica.investing import money


def main():
    if len(sys.argv) < 3:
        print("Usage: python -m analytica <present_value> <interest_rate> <time>")
        sys.exit(1)

    present_value, interest_rate, time = sys.argv[1], sys.argv[2], sys.argv[3]
    calculate = money.Calculate()
    fv = calculate.future_value_of_money(present_value, interest_rate, time)  # type: ignore
    print(Decimal(fv).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP"))


if __name__ == "__main__":
    main()
