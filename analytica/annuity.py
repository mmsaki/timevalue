import argparse

from analytica.investing import annuity

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

group0 = parser.add_mutually_exclusive_group()
group0.add_argument("--pv", action="store_true", help="present value")
group0.add_argument("--fv", action="store_true", help="future value")

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


def main():
    args = parser.parse_args()
    calculate = annuity.Annuity()
    if (
        args.present_value
        and not args.pv
        and not args.fv
        and not args.due
        and not args.growth_rate
    ):
        pv = calculate.present_value_of_annuity(
            args.cash_flow, args.interest_rate, args.time
        )
        return pv
    else:
        if (
            args.present_value
            and args.pv
            and not args.fv
            and not args.due
            and not args.growth_rate
        ):
            pv = calculate.present_value_of_annuity(
                args.cash_flow, args.interest_rate, args.time, args.pv
            )
            return pv
    if (
        args.present_value
        and args.due
        and not args.pv
        and not args.fv
        and not args.growth_rate
    ):
        pv = calculate.present_value_of_annuity_due(
            args.cash_flow, args.interest_rate, args.time
        )
        return pv
    else:
        if (
            args.present_value
            and args.pv
            and args.due
            and not args.fv
            and not args.growth_rate
        ):
            pv = calculate.present_value_of_annuity_due(
                args.cash_flow, args.interest_rate, args.time, args.pv
            )
            return pv

    if (
        args.present_value
        and args.growth_rate
        and not args.due
        and not args.pv
        and not args.fv
    ):
        pv = calculate.present_value_of_growing_annuity(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate
        )
        return pv
    else:
        if (
            args.present_value
            and args.growth_rate
            and args.pv
            and not args.due
            and not args.fv
        ):
            pv = calculate.present_value_of_growing_annuity(
                args.cash_flow, args.interest_rate, args.time, args.growth_rate, args.pv
            )
            return pv

    if (
        args.present_value
        and args.growth_rate
        and args.due
        and not args.pv
        and not args.fv
    ):
        pv = calculate.present_value_of_growing_annuity_due(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate
        )
        return pv
    else:
        if (
            args.present_value
            and args.growth_rate
            and args.due
            and args.pv
            and not args.fv
        ):
            pv = calculate.present_value_of_growing_annuity_due(
                args.cash_flow, args.interest_rate, args.time, args.growth_rate, args.pv
            )
            return pv

    if (
        args.future_value
        and not args.fv
        and not args.pv
        and not args.growth_rate
        and not args.due
    ):
        fv = calculate.future_value_of_annuity(
            args.cash_flow, args.interest_rate, args.time
        )
        return fv
    else:
        if (
            args.future_value
            and args.fv
            and not args.due
            and not args.growth_rate
            and not args.pv
        ):
            fv = calculate.future_value_of_annuity(
                args.cash_flow, args.interest_rate, args.time, args.fv
            )
            return fv
    if (
        args.future_value
        and args.due
        and not args.growth_rate
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_annuity_due(
            args.cash_flow, args.interest_rate, args.time
        )
        return fv
    else:
        if (
            args.future_value
            and args.due
            and args.fv
            and not args.growth_rate
            and not args.pv
        ):
            fv = calculate.future_value_of_annuity_due(
                args.cash_flow, args.interest_rate, args.time, args.fv
            )
            return fv
    if (
        args.future_value
        and args.growth_rate
        and not args.due
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_growing_annuity(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate
        )
        return fv
    else:
        if (
            args.future_value
            and args.growth_rate
            and args.fv
            and not args.due
            and not args.pv
        ):
            fv = calculate.future_value_of_growing_annuity(
                args.cash_flow, args.interest_rate, args.time, args.growth_rate, args.fv
            )
            return fv
    if (
        args.future_value
        and args.growth_rate
        and args.due
        and not args.fv
        and not args.pv
    ):
        fv = calculate.future_value_of_growing_annuity_due(
            args.cash_flow, args.interest_rate, args.time, args.growth_rate
        )
        return fv
    else:
        if (
            args.future_value
            and args.growth_rate
            and args.due
            and args.fv
            and not args.pv
        ):
            fv = calculate.future_value_of_growing_annuity_due(
                args.cash_flow, args.interest_rate, args.time, args.growth_rate, args.fv
            )
            return fv
