#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

def fib(n: int) -> int:
    """Calculate Fibonacci Number."""
    ret = 1
    if n == 0:
        return 0
    if n < 2:
        return ret
    state = [1, 1]
    for i in range(2, n):
        state[1] = state[0]
        state[0] = ret
        ret = state[0] + state[1]
    return ret

@click.command()
@click.argument('num', type=int)
def main(num: int):
    """Main entrypoint."""
    print(fib(num))

if __name__ == "__main__":
    main()
