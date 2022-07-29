#!/usr/bin/env python
from pathlib import Path
from re import MULTILINE, sub

import click
from pyperclip import copy
from tomli import loads


@click.command()
@click.option(
    "-c",
    "--config",
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help=".toml config",
)
def re_titles(config: Path) -> None:
    """
    Replace titles names from anidb.
    The result will be copied to the clipboard.

    \b
    >>> 1 	The Prince`s New Clothes
    <<< e1: EP1 «The Prince`s New Clothes»
    """
    titles = loads(config.read_text())["titles"]

    titles = sub(r"	", r" ", titles)
    titles = sub(r"  (.+?)\n", r" «\1»\n", titles)
    titles = sub(r" »", r"»", titles)
    titles = sub(r"^(\d+) ", r"e\1: EP\1 ", titles, flags=MULTILINE)
    titles = sub(r"^OP(\d+)", r"op\1: OP\1", titles, flags=MULTILINE)
    titles = sub(r"^ED(\d+)", r"ed\1: ED\1", titles, flags=MULTILINE)
    titles = sub(r"^S(\d+) ", r"s\1: S\1 ", titles, flags=MULTILINE)

    click.echo(titles)
    copy(titles)
