#!/usr/bin/env python3
from click import (
    group,
    option,
    argument,
    echo,
    pass_context,
    pass_obj,
    Choice
)
from utils.integrals import SimpleIntegral
from utils.derivatives import SimpleDerivative

@group()
@pass_context
def main(context):
    context.obj = 100

@main.command(help="Compute f'(x) for a simple polynomial f(x)")
@argument('x', type=float)
@option('--degree', type=Choice(['1', '2', '3', '4', '5']), default='1')
@pass_obj
def compute_derivative(obj, x, degree):
    obj_deriv = SimpleDerivative(x)
    if degree == '1':
        echo(obj_deriv.get_first_derivative())
    elif degree == '2':
        echo(obj_deriv.get_second_derivative())
    elif degree == '3':
        echo(obj_deriv.get_third_derivative())
    elif degree == '4':
        echo(obj_deriv.get_fourth_derivative())
    else:
        echo(obj_deriv.get_fifth_derivative())

@main.command(help='Compute F(x) for a simple polynomial f(x)')
@argument('x', type=float)
@option('--degree', type=Choice(['1', '2', '3', '4', '5']), default='1')
@pass_obj
def compute_integral(obj, x, degree):
    obj_integ = SimpleIntegral(x)
    if degree == '1':
        echo(obj_integ.get_first_integral())
    elif degree == '2':
        echo(obj_integ.get_second_integral())
    elif degree == '3':
        echo(obj_integ.get_third_integral())
    elif degree == '4':
        echo(obj_integ.get_fourth_integral())
    else:
        echo(obj_integ.get_fifth_integral())

if __name__ == '__main__':
    main()
