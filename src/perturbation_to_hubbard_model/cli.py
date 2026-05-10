"""Console script for pt_to_hubbard."""

import typer
from rich.console import Console

import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for pt_to_hubbard."""
    console.print("Replace this message by putting your code into pt_to_hubbard.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
