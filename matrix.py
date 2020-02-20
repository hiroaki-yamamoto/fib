#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import matrix_power as mat_pow
import click

def fib(n: int) -> int:
    """Calculate Fibonacci Number."""
    if n == 0:
        return 0
    mat = np.array([
        [1, 1],
        [1, 0]
    ], dtype=object)
    sol = mat_pow(mat, n)
    return sol[0, 1]

@click.command()
@click.argument('num', type=int)
def main(num: int):
    """Main entrypoint."""
    print(fib(num))

if __name__ == "__main__":
    main()
