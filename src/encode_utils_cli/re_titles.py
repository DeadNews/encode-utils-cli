from pathlib import Path
from re import MULTILINE, sub

import click
from pyperclip import copy as clipboard_copy
from tomli import loads


@click.command()
@click.option(
    "-c",
    "--config",
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help="Config in TOML format.",
)
@click.option(
    "--copy/--no-copy",
    is_flag=True,
    default=True,
    help="Copy the result to the clipboard.",
)
def re_titles(config: Path, copy: bool) -> None:
    """Reformat titles from AniDB.

    \f
    Example:

        >>> 1 	The Prince`s New Clothes
        <<< e1: EP1 «The Prince`s New Clothes»
    """  # noqa: D301
    titles = loads(config.read_text())["titles"]

    titles = sub(r"	", r" ", titles)
    titles = sub(r"  (.+?)\n", r" «\1»\n", titles)
    titles = sub(r" »", r"»", titles)
    titles = sub(r"^(\d+) ", r"e\1: EP\1 ", titles, flags=MULTILINE)
    titles = sub(r"^OP(\d+)", r"op\1: OP\1", titles, flags=MULTILINE)
    titles = sub(r"^ED(\d+)", r"ed\1: ED\1", titles, flags=MULTILINE)
    titles = sub(r"^S(\d+) ", r"s\1: S\1 ", titles, flags=MULTILINE)

    click.echo(titles)
    if copy:
        clipboard_copy(titles)
