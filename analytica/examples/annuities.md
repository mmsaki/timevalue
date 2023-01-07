# Introduction
<!-- [Reference](http://web.utk.edu/~jwachowi/growing_annuity.pdf) -->

- Annuity:
  - A series of equal payments or receipts occurring over a specified number of periods. In an ordinary annuity, payments or receipts occur at the end of each period; in an annuity due, payments or receipts occur at the beginning of each period.

- Growing Annuity:
  - A series of payments or receipts occurring over a specified number of periods that increase each period at a constant percentage. In a growing ordinary annuity, payments or receipts occur at the end of each period; in a growing annuity due, payments or receipts occur at the beginning of each period.

![Example](/images/fvga.jpg)

## Examples for annuity

The future value of a growing ordinary annuity (FVGA) answers questions like the following: "If R1 dollars, increasing each year at an annual rate g, are deposited in an account at the end of each year for n years, and if the deposits earn interest rate i compounded annually, what will be the value of the account at the end of n years?"

![Example Questions](/images/sample-examples.png)

## Example 1

You plan to retire in twenty years. If the annual (year-end) amount you save each year increases annually at a 6 percent rate (the growth rate of your income) and will be $1,000 initially at year end, and if you can earn 8 percent on your savings, how much will your retirement fund be worth in 20 years?

Answer: $72,691

```bash
annuity --future_value --cash_flow 1000 --growth_rate .06 --interest_rate 0.08 --time 20 
```

Output:

```bash
72691.08358182287
```

## Example 2

The annual end-of-year lease payments on a building increase 10 percent annually for the next 5 years. If 8 percent is an appropriate interest rate, and if the first year's lease payment is $10,000, what is the most an investor would pay to be the recipient of these lease payments?

Answer: $48,043

```bash
annuity --present_value --cash_flow 10000 --growth_rate .1 --interest_rate 0.08 --time 5
```

Output:

```bash
48043.0223274149
```

## Example 3

You wish to save annually an increasing (6% growth rate) amount (because your salary increases annually), and you wish to be worth $100,000 in 10 years. If you can earn 10% compounded annually on your savings, how much should your first (end-of-year) amount saved be?

Answer: $4,982

```bash
annuity --future_value --cash_flow 100000 --growth_rate .06 --interest_rate 0.1 --time 10 --fv
```

Output:

```bash
4981.972957798844
```

## Example 4

Your Uncle Harvey expects to live another 10 years. (Should he live longer, he feels you would be pleased to provide for him.) He currently has $50,000 in savings which he wishes to spread evenly in terms of purchasing power over the remainder of his life. Since he feels inflation will average 6 percent annually, his annual beginning-of-year withdrawals should increase at a 6% growth rate.
If he earns 8 percent on his savings not withdrawn, how much should his first withdrawal be? [Remember that the present value interest factor for a growing annuity due (PVIFGAD) is equal to the PVIFGA x (1 + i).]

Answer: $5,431

```bash
annuity --present_value --due --cash_flow 50000 --growth_rate .06 --interest_rate 0.08 --time 10 --pv
```

Output:

```bash
5430.936988345143
```
