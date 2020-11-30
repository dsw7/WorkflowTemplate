from math import factorial
from pytest import mark
from click.testing import CliRunner
from compute import (
    compute_derivative,
    compute_integral
)
from utils.consts import (
    EXIT_SUCCESS,
    MAX_DEGREE
)


@mark.test_command_line_interface
class TestCommandLineInterfaceDerivatives:
    def setup_class(self):
        self.runner = CliRunner()

    def test_compute_derivative_degree_1(self):
        result = self.runner.invoke(compute_derivative, '1.0 --degree 1'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 1)

    def test_compute_derivative_degree_2(self):
        result = self.runner.invoke(compute_derivative, '1.0 --degree 2'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 2)

    def test_compute_derivative_degree_3(self):
        result = self.runner.invoke(compute_derivative, '1.0 --degree 3'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 3)

    def test_compute_derivative_degree_4(self):
        result = self.runner.invoke(compute_derivative, '1.0 --degree 4'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 4)

    def test_compute_derivative_degree_5(self):
        result = self.runner.invoke(compute_derivative, '1.0 --degree 5'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 5)


@mark.test_command_line_interface
class TestCommandLineInterfaceIntegrals:
    def setup_class(self):
        self.runner = CliRunner()

    def test_compute_integral_degree_1(self):
        result = self.runner.invoke(compute_integral, '1.0 --degree 1'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 4)

    def test_compute_integral_degree_2(self):
        result = self.runner.invoke(compute_integral, '1.0 --degree 2'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 3)

    def test_compute_integral_degree_3(self):
        result = self.runner.invoke(compute_integral, '1.0 --degree 3'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 2)

    def test_compute_integral_degree_4(self):
        result = self.runner.invoke(compute_integral, '1.0 --degree 4'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE - 1)

    def test_compute_integral_degree_5(self):
        result = self.runner.invoke(compute_integral, '1.0 --degree 5'.split())
        assert result.exit_code == EXIT_SUCCESS
        assert float(result.output.strip()) == 1 / factorial(MAX_DEGREE)
