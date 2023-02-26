import argparse

from timevalue.investing import annuity

parser = argparse.ArgumentParser(
    description="Calculate annuity payments.", conflict_handler="resolve"
)

parser.add_argument("-c", "--cash_flow", type=float, help="Cash flow", metavar="")

group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-p",
    "--present_value",
    action="store_true",
    help="present value",
)
group.add_argument(
    "-f",
    "--future_value",
    action="store_true",
    help="future value",
)


parser.add_argument(
    "-i",
    "--interest_rate",
    type=float,
    required=True,
    help="interest rate",
    metavar="",
)
parser.add_argument("-t", "--time", required=True, type=int, help="time", metavar="")
parser.add_argument(
    "-d",
    "--due",
    action="store_true",
    help="With an annuity due, payments are made at the beginning of each period",
)

parser.add_argument(
    "-g",
    "--growth_rate",
    type=float,
    help="growth rate",
    metavar="",
)

reversed = parser.add_mutually_exclusive_group()
reversed.add_argument(
    "--pv", action="store_true", help="reverse calculate the present value (bool)"
)
reversed.add_argument(
    "--fv", action="store_true", help="reverse calculate the future value (bool)"
)

args = parser.parse_args()


def ordinary_annuity():
    calculate = annuity.Annuity(args.cash_flow, args.interest_rate, args.time)
    if (
        args.present_value
        and not args.pv
        and not args.fv
        and not args.due
        and not args.growth_rate
    ):
        pv = calculate.present_value_of_annuity()
        return pv
    else:
        if (
            args.present_value
            and args.pv
            and not args.fv
            and not args.due
            and not args.growth_rate
        ):
            pv = calculate.present_value_of_annuity(pv=True)
            return pv
    if (
        args.present_value
        and args.due
        and not args.pv
        and not args.fv
        and not args.growth_rate
    ):
        pv = calculate.present_value_of_annuity_due()
        return pv
    else:
        if (
            args.present_value
            and args.pv
            and args.due
            and not args.fv
            and not args.growth_rate
        ):
            pv = calculate.present_value_of_annuity_due(pv=True)
            return pv

    if (
        args.future_value
        and not args.fv
        and not args.pv
        and not args.growth_rate
        and not args.due
    ):
        fv = calculate.future_value_of_annuity()
        return fv
    else:
        if (
            args.future_value
            and args.fv
            and not args.due
            and not args.growth_rate
            and not args.pv
        ):
            fv = calculate.future_value_of_annuity(fv=True)
            return fv
    if (
        args.future_value
        and args.due
        and not args.growth_rate
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_annuity_due()
        return fv
    else:
        if (
            args.future_value
            and args.due
            and args.fv
            and not args.growth_rate
            and not args.pv
        ):
            fv = calculate.future_value_of_annuity_due(fv=True)
            return fv


def growing_annuity():
    calculate = annuity.GrowingAnnuity(
        args.cash_flow, args.interest_rate, args.growth_rate, args.time
    )
    if (
        args.present_value
        and args.growth_rate
        and not args.due
        and not args.pv
        and not args.fv
    ):
        pv = calculate.present_value_of_growing_annuity()
        return pv
    else:
        if (
            args.present_value
            and args.growth_rate
            and args.pv
            and not args.due
            and not args.fv
        ):
            pv = calculate.present_value_of_growing_annuity(pv=True)
            return pv

    if (
        args.present_value
        and args.growth_rate
        and args.due
        and not args.pv
        and not args.fv
    ):
        pv = calculate.present_value_of_growing_annuity_due()
        return pv
    else:
        if (
            args.present_value
            and args.growth_rate
            and args.due
            and args.pv
            and not args.fv
        ):
            pv = calculate.present_value_of_growing_annuity_due(pv=True)
            return pv

    if (
        args.future_value
        and args.growth_rate
        and not args.due
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_growing_annuity()
        return fv
    else:
        if (
            args.future_value
            and args.growth_rate
            and args.fv
            and not args.due
            and not args.pv
        ):
            fv = calculate.future_value_of_growing_annuity(fv=True)
            return fv
    if (
        args.future_value
        and args.growth_rate
        and args.due
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_growing_annuity_due()
        return fv
    else:
        if (
            args.future_value
            and args.growth_rate
            and args.due
            and args.fv
            and not args.pv
        ):
            fv = calculate.future_value_of_growing_annuity_due(fv=True)
            return fv


def main():
    if not args.growth_rate:
        print(ordinary_annuity())
    else:
        print(growing_annuity())


if __name__ == "__main__":
    main()
