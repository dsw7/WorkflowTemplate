from os import path
from tempfile import gettempdir
import nox

PATH_TO_PROJECT = path.dirname(__file__)
PYTHON_INTERP_VERSION = '3.6.10'

nox.options.envdir = path.join(gettempdir(), '.nox_workflow_template')
nox.options.report = path.join(nox.options.envdir, 'nox_report_workflow_template')

@nox.session(python=PYTHON_INTERP_VERSION)
def lint(session):
    command = 'pylint {} {} --output-format=colorized --exit-zero --rcfile {}'.format(
        PATH_TO_PROJECT, path.join(PATH_TO_PROJECT, 'utils'), path.join(PATH_TO_PROJECT, 'configs/pylint.rc')
    )
    msg_template = ['--msg-template', '{msg_id}{line:4d}{column:3d} {obj} {msg}']
    session.install('-r', path.join(PATH_TO_PROJECT, 'requirements.txt'))
    session.run(*command.split(), *msg_template, external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def run_pytests_integral_tests(session):
    command = 'pytest -vs {} -c {} -m test_integrals'.format(PATH_TO_PROJECT, path.join(PATH_TO_PROJECT, 'configs/pytest.ini'))
    session.install('-r', path.join(PATH_TO_PROJECT, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def run_pytests_derivative_tests(session):
    command = 'pytest -vs {} -c {} -m test_derivatives'.format(PATH_TO_PROJECT, path.join(PATH_TO_PROJECT, 'configs/pytest.ini'))
    session.install('-r', path.join(PATH_TO_PROJECT, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def compute_cyclomatic_complexity(session):
    command = 'radon cc {}'.format(PATH_TO_PROJECT)
    session.install('-r', path.join(PATH_TO_PROJECT, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def compute_maintainability_index(session):
    command = 'radon mi {} --show'.format(PATH_TO_PROJECT)
    session.install('-r', path.join(PATH_TO_PROJECT, 'requirements.txt'))
    session.run(*command.split(), external=True)
