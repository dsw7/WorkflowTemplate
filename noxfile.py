from os import path, environ
from tempfile import gettempdir
from dotenv import load_dotenv
import nox

load_dotenv()
nox.options.envdir = path.join(gettempdir(), 'nox_workflow_template')
nox.options.report = path.join(nox.options.envdir, 'noxreport')
nox.options.reuse_existing_virtualenvs = True

PROJECT_HOME = environ['PROJECT_HOME']
PATH_CONFIGS = environ['PATH_CONFIGS']
PYTHON_INTERP_VERSION = '3.6.10'

@nox.session(python=PYTHON_INTERP_VERSION)
def lint(session):
    command = 'pylint {} {} --output-format=colorized --exit-zero --rcfile {}'.format(
        PROJECT_HOME, path.join(PROJECT_HOME, 'src'), path.join(PATH_CONFIGS, 'pylint.rc')
    )
    msg_template = ['--msg-template', '{msg_id}{line:4d}{column:3d} {obj} {msg}']
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), *msg_template, external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def test_integral(session):
    command = 'pytest -vs {} -c {} -m test_integrals'.format(PROJECT_HOME, path.join(PATH_CONFIGS, 'pytest.ini'))
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def test_derivative(session):
    command = 'pytest -vs {} -c {} -m test_derivatives'.format(PROJECT_HOME, path.join(PATH_CONFIGS, 'pytest.ini'))
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def test_cli(session):
    command = 'pytest -vs {} -c {} -m test_command_line_interface'.format(PROJECT_HOME, path.join(PATH_CONFIGS, 'pytest.ini'))
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def compute_cyclomatic_complexity(session):
    command = 'radon cc {}'.format(PROJECT_HOME)
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), external=True)

@nox.session(python=PYTHON_INTERP_VERSION)
def compute_maintainability_index(session):
    command = 'radon mi {} --show'.format(PROJECT_HOME)
    session.install('-r', path.join(PROJECT_HOME, 'requirements.txt'))
    session.run(*command.split(), external=True)
