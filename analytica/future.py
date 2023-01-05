import argparse
from analytica.investing import time_value_money
from decimal import Decimal

parser = argparse.ArgumentParser(description="Calculate future value of money.")
parser.add_argument("present_value", type=float, help="present value")
parser.add_argument("interest_rate", type=float, help="interest rate")
parser.add_argument("time", type=int, help="time")

def main():
    args = parser.parse_args()
    calculate = time_value_money.TimeValueOfMoney()
    fv = calculate.future_value_of_money(args.present_value, args.interest_rate, args.time)  # type: ignore
    print(Decimal(fv).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP"))


if __name__ == "__main__":
    main()
