# Contributing

Before making changes create a virtual environment

```bash
python -m venv venv
```

Notice that a `/venv` directory is created in the project folder. Activate the virtual environemnt:

```bash
source ./venv/bin/activate
```

Next, install package using with `-e` flag for development

```bash
python -m pip install -e .
```

Run test:

```bash
pytest
```

## Build

Install build

```bash
python -m pip install --upgrade build
```

Build package project

```bash
python -m build
```

## Distribution

You’ll need to install Twine:

```bash
python -m pip install --upgrade twine
```

For test distribution use testpypi:

```bash
python -m twine upload --repository testpypi dist/*
```

## Versioning

Install setuptools-git-versioning:

```bash
pip install setuptools-git-versioning
```

Checking dirty and beta versions for project using [setuptools-git-versioning](https://setuptools-git-versioning.readthedocs.io/en/stable/)

Run:

```bash
python -m setuptools_git_versioning
```
