from math import factorial
from pytest import mark
from derivatives import SimpleDerivative
from consts import MAX_DEGREE

@mark.test_derivatives
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_first_derivative(x):
    degree = MAX_DEGREE - 1
    coefficient = 1 / factorial(degree)
    assert SimpleDerivative(x).get_first_derivative() == coefficient * x ** degree

@mark.test_derivatives
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_second_derivative(x):
    degree = MAX_DEGREE - 2
    coefficient = 1 / factorial(degree)
    assert SimpleDerivative(x).get_second_derivative() == coefficient * x ** degree

@mark.test_derivatives
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_third_derivative(x):
    degree = MAX_DEGREE - 3
    coefficient = 1 / factorial(degree)
    assert SimpleDerivative(x).get_third_derivative() == coefficient * x ** degree

@mark.test_derivatives
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_fourth_derivative(x):
    degree = MAX_DEGREE - 4
    coefficient = 1 / factorial(degree)
    assert SimpleDerivative(x).get_fourth_derivative() == coefficient * x ** degree

@mark.test_derivatives
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_fifth_derivative(x):
    degree = MAX_DEGREE - 5
    coefficient = 1 / factorial(degree)
    assert SimpleDerivative(x).get_fifth_derivative() == coefficient * x ** degree
