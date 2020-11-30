# WorkflowTemplate
The majority of my programming experience has revolved around designing command line programs.
In this repository, I provide a template approximating my day-to-day workflow, including which frameworks I commonly use.

## The dummy program
In this template, I have provided a basic command line program, `foobar`, which computes:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?f^{(-n)}(x);\&space;\forall&space;n\in&space;\{1,...,5\}">
</p>
For the primary starting linear equation:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?f(x)=x">
</p>
The program also computes:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?g^n(x);\&space;\forall&space;n\in&space;\{1,...,5\}">
</p>
The secondary equation is the fifth antiderivative of the first linear equation:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?g(x)=f^{(-5)}(x)=\frac{1}{720}x^6">
</p>

## The command line interface
I use [click](https://click.palletsprojects.com/en/7.x/) for creating all my command line programs.

## Workflow automation
I use [nox](https://nox.thea.codes/en/stable/) for automating my workflows. My workflows almost always consist of extensive testing, code complexity analysis and static code analysis. Some projects also include `nox` sessions for automating compilation, such as complex cases involving C++ code that is tested using a Python testing framework.  

## Static code analysis
I use [pylint](https://www.pylint.org/) to catch obvious issues with my code. I like fine grained control over my linters using a `pylint.rc` file which I keep under `configs`. 

## Testing
I use [pytest](https://docs.pytest.org/en/stable/) for all testing. I like to separate my tests into logical groups using markers. I like fine grained control over my tests using a `pytest.ini` file which I keep under `configs`.

## Complexity and maintainability analysis
I use [radon](https://radon.readthedocs.io/en/latest/index.html) for evaluating the complexity and maintainability of my programs. I'm particularly interested in evaluating the [maintainability index](https://en.wikipedia.org/wiki/Maintainability) and [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) of my programs because I feel these metrics help enforce better, cleaner code.
