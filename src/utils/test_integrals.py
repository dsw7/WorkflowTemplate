from math import factorial
from pytest import mark
from integrals import SimpleIntegral
from consts import MAX_DEGREE

@mark.test_integrals
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_first_integral(x):
    degree = MAX_DEGREE - 4
    coefficient = 1 / factorial(degree)
    assert SimpleIntegral(x).get_first_integral() == coefficient * x ** degree

@mark.test_integrals
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_second_integral(x):
    degree = MAX_DEGREE - 3
    coefficient = 1 / factorial(degree)
    assert SimpleIntegral(x).get_second_integral() == coefficient * x ** degree

@mark.test_integrals
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_third_integral(x):
    degree = MAX_DEGREE - 2
    coefficient = 1 / factorial(degree)
    assert SimpleIntegral(x).get_third_integral() == coefficient * x ** degree

@mark.test_integrals
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_fourth_integral(x):
    degree = MAX_DEGREE - 1
    coefficient = 1 / factorial(degree)
    assert SimpleIntegral(x).get_fourth_integral() == coefficient * x ** degree

@mark.test_integrals
@mark.parametrize(
    'x', list(range(1, 6)), ids=list(f'x = {i}' for i in range(1, 6))
)
def test_fifth_integral(x):
    degree = MAX_DEGREE
    coefficient = 1 / factorial(degree)
    assert SimpleIntegral(x).get_fifth_integral() == coefficient * x ** degree
