#!/usr/bin/env python3
from decimal import *
import sys


def nilakantha_terms():
    """
    Generate the terms of the Nilakantha series for pi.
    """
    yield 3
    d = Decimal(2)
    sign = 1
    while True:
        yield sign * 4 / (d * (d + 1) * (d + 2))
        d += 2
        sign *= -1


def pi(error):
    """
    Calculate pi using the Nilakantha series, stopping when terms become
    smaller than `error`.
    """
    pi = Decimal(0)
    for term in nilakantha_terms():
        pi += term
        if abs(term) < error:
            return pi


def power_of_ten(n):
    """
    Return 0.1^n as a Decimal, suitable for feeding to Decimal.quantize().

    We can't just do Decimal(0.1 ** n), because Decimals get their internal
    idea of their precision from their string constructors, and creating one
    from a float interferes with that.
    """
    return Decimal('0.' + '0' * (n - 1) + '1')


def main():
    """
    Calculate pi to a number of decimal places given by the first command-line
    argument.
    """
    precision = int(sys.argv[1])
    error = power_of_ten(precision + 1)
    rounder = power_of_ten(precision)
    print(pi(error).quantize(rounder, rounding=ROUND_HALF_UP))

if __name__ == "__main__":
    main()
