# Perturbation to Hubbard Model

![PyPI version](https://img.shields.io/pypi/v/Perturbation-to-Hubbard-Model.svg)

The Perturbation to Hubbard Model package constructs a circuit which calculates the first order corrections to the two-electron Hubbard model. The perturbation is constructed based on the addition of dipole-dipole int

* [GitHub](https://github.com/MyaBird/Perturbation-to-Hubbard-Model/) | [PyPI](https://pypi.org/project/Perturbation-to-Hubbard-Model/) | [Documentation](https://MyaBird.github.io/Perturbation-to-Hubbard-Model/)
* Created by [Mya G. Shekitka](https://audrey.feldroy.com/) | GitHub [@MyaBird](https://github.com/MyaBird) | PyPI [@MyaBird](https://pypi.org/user/MyaBird/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://MyaBird.github.io/Perturbation-to-Hubbard-Model/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/Perturbation-to-Hubbard-Model.git
cd Perturbation-to-Hubbard-Model

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `pt_to_hubbard`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

Perturbation to Hubbard Model was created in 2026 by Mya G. Shekitka.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
