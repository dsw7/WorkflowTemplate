# WorkflowTemplate
## Table of Contents
  # [Introduction](#introduction)  
  # [The dummy program](#the-dummy-program)  
## Introduction
The majority of my programming experience has revolved around designing command line programs.
In this repository, I provide a template approximating my day-to-day workflow, including which frameworks I commonly use. Here you will find examples of how I implement test and build automation, how and where I put my tests, how I set my tests up, how I lint my code, among others. 

## The dummy program
In this template, I have provided a basic command line program, `foobar`, which computes the antiderivative:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?f^{(-n)}(x);\&space;\forall&space;n\in&space;\{1,...,5\}">
</p>

For the simple function _f_:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?f(x)=x">
</p>

For example the command:
```
$ src/foobar.py compute-integral 1 --degree 3
0.041666666666666664
```
Computes the third antiderivative of _f_ at _x_ = 1:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?f^{(-3)}(1)=\frac{1}{24}1^4=\frac{1}{24}">
</p>

The program also computes the derivative of a function _g_:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?g^n(x);\&space;\forall&space;n\in&space;\{1,...,5\}">
</p>

Where _g_ is the fifth antiderivative of _f_:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?g(x)=f^{(-5)}(x)=\frac{1}{720}x^6">
</p>

For example the command:
```
$ src/foobar.py compute-derivative 1 --degree 3
0.16666666666666666
```
Computes the third derivative of _g_ at _x_ = 1:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?g^3(1)=\frac{1}{6}(1)^3=\frac{1}{6}">
</p>

## What a useless program?
I said dummy program. I didn't say useful program. All though I suppose a pair of `compute-integral` invocations could be used to compute the definite integral of _f_.

## The command line interface
I use [click](https://click.palletsprojects.com/en/7.x/) for creating all my command line programs. I could explain why I prefer `click` over some other related libraries, but `click` does a pretty good job marketing itself: [Why Click?](https://click.palletsprojects.com/en/7.x/why/#why-not-argparse)

## Workflow automation
I use [nox](https://nox.thea.codes/en/stable/) for automating my workflows. My workflows almost always consist of extensive testing, code complexity analysis and static code analysis. Some projects also include `nox` sessions for automating compilation, such as complex cases involving C++ code that is tested using a Python testing framework.

## Getting the program requirements
The `nox` automation framework creates a virtual environment and installs required dependencies on a per session basis. I like to use a `requirements.txt` file to specify these dependencies. To get a `requirements.txt` file, I use `pipreqs`:
```
pipreqs /path/to/project --force
```

## Static code analysis
I use [pylint](https://www.pylint.org/) to catch obvious issues with my code. I like fine grained control over my linters. To allow for small tweaks, I use a `pylint.rc` file which I keep under the `configs` directory.

## Testing
I use [pytest](https://docs.pytest.org/en/stable/) for all testing. I like to separate my tests into logical groups using markers. I like fine grained control over my tests. To make small tweaks, I use a `pytest.ini` file which I keep under the `configs` directory. 

## Complexity and maintainability analysis
I use [radon](https://radon.readthedocs.io/en/latest/index.html) for evaluating the complexity and maintainability of my programs. I'm particularly interested in evaluating the [maintainability index](https://en.wikipedia.org/wiki/Maintainability) and [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) of my programs because I feel these metrics help enforce better, cleaner code.

## Environment variable management
I think environment variables can be very useful in certain cases. For example, referencing a project's "home" directory from somewhere deep within a very nested project. I use [dotenv](https://www.npmjs.com/package/dotenv) for managing environment variables and I like to place the `.env` file in the project's home directory. In this template, I define the path to the project home and the project configuration file directories as a set of environment variables in the `.env` file. I then reference the environment variables in `noxfile.py`.
