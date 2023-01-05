import argparse
from analytica.investing import annuity

parser = argparse.ArgumentParser(
    description='Calculate annuity payments.', conflict_handler='resolve')
parser.add_argument('cash_flow', type=float, help='Cash flow')
parser.add_argument('interest_rate', type=float, help='interest rate')
parser.add_argument('time', type=int, help='time')
parser.add_argument('-d', '--due', action="store_true",
                    help='With an annuity due, payments are made at the beginning of each period',
                    )
parser.add_argument('-f', '--future_value',
                    action="store_true", help='future value',)
parser.add_argument('-p', '--present_value',
                    action="store_true", help='present value',)
parser.add_argument('-g', '--growth_rate', type=float, action="store", help='growth rate',)


def main():
    args = parser.parse_args()
    calculate = annuity.Annuity()
    if args.due and args.future_value:
        fv = calculate.future_value_of_annuity_due(
            args.cash_flow, args.interest_rate, args.time)
        return fv
    if not args.due and args.future_value:
        fv = calculate.future_value_of_annuity(
            args.cash_flow, args.interest_rate, args.time)
        return fv
    if args.due and args.present_value:
        pv = calculate.present_value_of_annuity_due(
            args.cash_flow, args.interest_rate, args.time)
        return pv
    if not args.due and args.present_value:
        pv = calculate.present_value_of_annuity(
            args.cash_flow, args.interest_rate, args.time)
        return pv
    if not args.due and args.future_value and args.growth_rate:
        fv = calculate.future_value_of_growing_annuity(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate)
        return fv
    if args.future_value and args.growth_rate and args.due:
        fv = calculate.future_value_of_growing_annuity_due(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate)
        return fv
    if not args.due and args.present_value and args.growth_rate:
        pv = calculate.present_value_of_growing_annuity(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate)
        return pv
    if args.present_value and args.growth_rate and args.due:
        pv = calculate.present_value_of_growing_annuity_due(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate)
        return pv


if __name__ == "__main__":
    main()
