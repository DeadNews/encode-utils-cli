from fractions import Fraction
from pathlib import PurePath
from re import search

import click
from pyperclip import copy as clipboard_copy

from encode_utils_cli.util.timeconv import ts2f


@click.command()
@click.argument(
    "screens",
    nargs=-1,
    required=True,
    type=click.Path(dir_okay=False, path_type=PurePath),
)
@click.option("-f", "--fps", type=str, default="24000/1001")
@click.option(
    "--copy/--no-copy",
    is_flag=True,
    default=True,
    help="Copy the result to the clipboard.",
)
def screens2bm(screens: tuple[PurePath], fps: str, copy: bool) -> None:
    """Convert `hh:mm:ss.xxxx` in screens filenames to bookmark frames.

    \f
    Example:

        >>> 00000 (00:12:34.34) 01.png
        <<< 18086
        >>> 00000 (00_00_03.34) 02.png
        <<< 80
    """  # noqa: D301
    frames = [
        f"{ts2f(ts=ts.group(1).replace('_', ':'), fps=Fraction(fps))}"
        for screen in screens
        if (ts := search(r"(\d+[:_]\d+[:_]\d+\.\d+)", screen.stem))
    ]
    bookmark = ", ".join(frames) + "\n"
    click.echo(bookmark)
    if copy:
        clipboard_copy(bookmark)
