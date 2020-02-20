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
    ret = fib(n - 1) + fib(n - 2)
    return ret

@click.command()
@click.argument('num', type=int)
def main(num: int):
    """Main entrypoint."""
    print(fib(num))

if __name__ == "__main__":
    main()
