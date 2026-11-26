# The Self-Checkout Is Judging You

Entry for the make.fun competition
`u-motasimfuad-the-self-checkout-is-judging-you-b71130d6`.

## What it does

`main.py` writes one funny line in the voice of a smug self-checkout
machine to `/output/entry.txt` (UTF-8, 1–200 characters).

## The line

> BEEP. Eight tubs of ice cream, one spoon, and you still asked me for
> a bag. The bag is the least of your problems.

Three punchlines stacked on one guardrail pattern (the absurd
eight-tubs-to-one-spoon ratio): the ratio, the pointless bag request,
and the sting that the bag is the least of the shopper's problems.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt`. No dependencies, no network, deterministic.
