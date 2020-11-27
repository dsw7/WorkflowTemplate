#!/usr/bin/env python3
from click import (
    group,
    argument,
    echo,
    pass_context,
    pass_obj
)

@group()
@pass_context
def main(context):
    context.obj = 100

@main.command(help='Add two numbers')
@argument('x', type=int)
@argument('y', type=int)
@pass_obj  # <- gets obj from the main context.obj invocation
def add_two_numbers(obj, x, y):
    echo(f'The sum is {x + y + obj}')

@main.command(help='Subtract two numbers')
@argument('x', type=int)
@argument('y', type=int)
@pass_obj
def subtract_two_numbers(obj, x, y):
    echo(f'The difference is {x - y - obj}')

if __name__ == '__main__':
    main()
