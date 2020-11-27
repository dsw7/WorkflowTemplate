from pytest import mark
from click.testing import CliRunner
from compute import (
    compute_derivative,
    compute_integral
)

@mark.test_command_line_interface
class TestCommandLineInterface:
    def setup_class(self):
        self.runner = CliRunner()

    def test_compute_derivative(self):
        result = self.runner.invoke(compute_derivative, ['5.0', '--degree', '5'])
        assert result.exit_code == 0
    
    def test_compute_integral(self):
        result = self.runner.invoke(compute_integral, ['5.0', '--degree', '5'])
        assert result.exit_code == 0
