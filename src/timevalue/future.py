import argparse

from timevalue.investing import time_value_money

parser = argparse.ArgumentParser(description="Calculate future value of money.")
parser.add_argument("cash_flow", type=float, help="present value")
parser.add_argument("interest_rate", type=float, help="interest rate")
parser.add_argument("time", type=int, help="time")


def main():
    args = parser.parse_args()
    calculate = time_value_money.TimeValueOfMoney(
        args.cash_flow, args.interest_rate, args.time
    )
    fv = calculate.future_value_of_money()
    print(round(fv, 2))


if __name__ == "__main__":
    main()
