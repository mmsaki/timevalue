import argparse
from analytica.investing import annuity

parser = argparse.ArgumentParser(description='Calculate annuity payments.')
parser.add_argument('present_value', type=float, help='present value')
parser.add_argument('interest_rate', type=float, help='interest rate')
parser.add_argument('time', type=int, help='time')

def main():
    args = parser.parse_args()
    calculate = annuity.Annuity()
    fv = calculate.future_value_of_annuity(
        args.present_value, args.interest_rate, args.time)
    print(fv)


if __name__ == "__main__":
    main()
