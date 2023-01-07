import argparse

from analytica.investing import annuity

parser = argparse.ArgumentParser(
    description="Calculate annuity payments.", conflict_handler="resolve"
)
parser.add_argument("-c", "--cash_flow", type=float, help="Cash flow", metavar="")
parser.add_argument(
    "-i",
    "--interest_rate",
    type=float,
    help="interest rate",
    metavar="",
)
parser.add_argument("-t", "--time", type=int, help="time", metavar="")
parser.add_argument(
    "-f",
    "--future_value",
    type=float,
    help="future value",
    metavar="",
)
parser.add_argument(
    "-p",
    "--present_value",
    type=float,
    help="present value",
    metavar="",
)
parser.add_argument(
    "-g",
    "--growth_rate",
    type=float,
    help="growth rate",
    metavar="",
)
parser.add_argument(
    "-d",
    "--due",
    action="store_true",
    help="With an annuity due, payments are made at the beginning of each period",
)


def main():
    args = parser.parse_args()
    calculate = annuity.Annuity()
    if args.due and args.future_value and not args.growth_rate:
        fv = calculate.future_value_of_annuity_due(
            args.future_value, args.interest_rate, args.time
        )
        return fv
    if not args.due and args.future_value and not args.growth_rate:
        fv = calculate.future_value_of_annuity(
            args.future_value, args.interest_rate, args.time
        )
        return fv
    if args.due and args.present_value and not args.growth_rate:
        pv = calculate.present_value_of_annuity_due(
            args.present_value, args.interest_rate, args.time
        )
        return pv
    if not args.due and args.present_value and not args.growth_rate:
        pv = calculate.present_value_of_annuity(
            args.present_value, args.interest_rate, args.time
        )
        return pv
    if not args.due and args.future_value and args.growth_rate:
        fv = calculate.future_value_of_growing_annuity(
            args.future_value, args.interest_rate, args.time, args.growth_rate
        )
        return fv
    if args.future_value and args.growth_rate and args.due:
        fv = calculate.future_value_of_growing_annuity_due(
            args.future_value, args.interest_rate, args.time, args.growth_rate
        )
        return fv
    if not args.due and args.present_value and args.growth_rate:
        pv = calculate.present_value_of_growing_annuity(
            args.present_value, args.interest_rate, args.time, args.growth_rate
        )
        return pv
    if args.present_value and args.growth_rate and args.due:
        pv = calculate.present_value_of_growing_annuity_due(
            args.present_value, args.interest_rate, args.time, args.growth_rate
        )
        return pv
