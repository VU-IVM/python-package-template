# Enhancing reproducibility and scalability with pyproject.toml

This manual has been written with the purpose of guiding the reader through the process of installing software using pip install .e accompanied by a pyproject.toml file.

## Why?

### Why pip install -e?

We want to install our software package as pip install -e (short for --editable) because as developers we want to implement and test changes iteratively, before cutting a release and preparing a distribution archive. 

To facilitate iterative exploration and experimentation, setuptools allows users to instruct the Python interpreter and its import machinery to load the code under development directly from the project folder without having to copy the files to a different location in the disk. This means that changes in the Python source code can immediately take place without requiring a new installation.

You can enter this “development mode” by performing an editable installation inside of a virtual environment, using pip’s -e/--editable flag, as shown below:

```
cd your-python-project
conda create --name your-python-project
```
Activate your environemt with:
`conda activate your-python-project`


`pip install --editable . `

Now you have access to your package
as if it was installed in the your_python_project environment"
`from your-python-project import your-module`


An “editable installation” works very similarly to a regular install with pip install ., except that it only installs your package dependencies, metadata and wrappers for console and GUI scripts. Under the hood, setuptools will try to create a special .pth file in the target directory (usually site-packages) that extends the PYTHONPATH or install a custom import hook.

(from: https://setuptools.pypa.io/en/latest/userguide/development_mode.html )

### Why pyproject.toml?

The pyproject.tom file was introduced as part of the Python Enhancement Proposal (PEP) 518, that specifies how Python projects must specify build dependencies.

These build dependeencies will be stored in the file that is located at the root directory of the project and follows the TOML (Tom’s Obvious, Minimal Language) syntax.

It contains metadata information such as the project name, version, description, author, license, and various other details.

One of the key features of the pyproject.toml file is the ability to define project dependencies. This allows developers to specify the packages and their versions required for the project to run properly. This helps in maintaining the consistency of the project and ensures that the project can be easily reproduced by other developers.

The pyproject.toml file also supports the concept of extras which allows developers to define optional dependencies for a project. This allows users to install only the necessary dependencies in order to run the project. Usually, in the extras section one could specify additional requirements that will be used as part of testing (e.g. pytest).

In addition to the standard metadata and dependencies, pyproject.toml file also supports custom fields that can be used by third-party tools. As an example, you can consider linters, formatters and checkers such as black and mypy. This allows developers to extend the functionality of the file and add custom fields as per their requirements.

(from: https://towardsdatascience.com/pyproject-python-9df8cc092f61 )

## Instructions

There are two complications before starting:

If you install the developer dependencies, ruff will be installed. In short, ruff is an extremely fast Python linter, written in Rust. More info here. Ruff is written in rust, so you need to install rust by curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

for cartopy, the pip building wheel cannot find geos for mac m1, so I installed geos by: brew install geos.

Create a new environment with mamba/conda. I you do not have mamba and/or miniforge yet, install them first. You can also do this with venv. I used: 

`conda create --name your-python-project "python<=3.10"`

activate the new environment

`conda activate your-python-project`

inside the main dir of the cloned environment type in terminal (mac/linux): 

`pip install -e .'[dev]'  `

or pip install -e . [dev] (windows) (or without dev if you don't want to have those developer dependencies. However, they contain hatch and ruff which we want as developers.)

## Create documentation

`pip install -e .'[docs]'

`mkdir docs`

`cd docs`

`sphinx-quickstart`

Enter now when they ask you to split source and output directory. 

Now edit config.py:

Add extensions:
```
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "autoapi.extension",
    "myst_parser",
]
```

```
# -- Use autoapi.extension to run sphinx-apidoc -------

autoapi_dirs = ["../s2spy"]
```

Now execute the docs build commands that are listed in pyproject toml using:
```
hatch run docs:build
```

To publish it online:

add .readthedocs.yaml
```
version: 2

build:
  os: ubuntu-20.04
  tools:
    python: "3.9"

python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs
```
Sign into https://readthedocs.org/. 

Select your repository, and it will be build.

## Sources
https://setuptools.pypa.io/en/latest/userguide/development_mode.html 

https://towardsdatascience.com/pyproject-python-9df8cc092f61
