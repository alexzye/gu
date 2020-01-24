# gux
git user switcher

## Installation
`gux` is written in Python3 and uses pip3 for installation.

```bash
pip3 intall gux
```

## Usage

`gux` has the following commands: 'use', 'add', 'list', 'ls', 'rm'.

`gux use [user]` - Changes the main tracked user used by `gux`
`gux rm [user]`  - Deletes a user from the `gux` registry
`gux add`        - Adds a new user to the `gux` registry
`gux list`       - Lists the current git configurations in a repo
`gux ls`         - Show list of current users registered to gux

## Development
Use `pipenv` to isolate your development environment. Run the following from the project root:

```bash
pipenv shell --python=`which python3`
```

In your `pipenv` environment, install `gux` manaully:

Note: Replace the X with the current gux verion.

```bash
python setup.py sdist bdist_wheel && pip install --upgrade --force-reinstall dist/gux-0.0.X-py3-none-any.whl
```

To upload the app to pypi:

```bash
python3 setup.py sdist bdist_wheel && python3 -m twine upload dist/*
```