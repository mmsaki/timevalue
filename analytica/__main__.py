import argparse

from analytica.investing import time_value_money


def main():
    parser = argparse.ArgumentParser(description="Calculate present value of money.")
    parser.add_argument("future_value", type=float, help="future value")
    parser.add_argument("interest_rate", type=float, help="interest rate")
    parser.add_argument("time", type=int, help="time")
    args = parser.parse_args()
    calculate = time_value_money.TimeValueOfMoney(
        args.future_value, args.interest_rate, args.time
    )
    fv = calculate.present_value_of_money()
    print(round(fv, 2))


if __name__ == "__main__":
    main()
