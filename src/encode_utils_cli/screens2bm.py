#!/usr/bin/env python
from fractions import Fraction
from pathlib import PurePath
from re import search

import click
from pyperclip import copy

from .util.timeconv import ts2f


@click.command()
@click.argument(
    "screens",
    nargs=-1,
    required=True,
    type=click.Path(dir_okay=False, path_type=PurePath),
)
@click.option("-f", "--fps", type=str, default="24000/1001")
def screens2bm(screens: tuple[PurePath], fps: str) -> None:
    """
    Parse screens timestamps hh:mm:ss.xxxx into bookmark format.
    The result will be copied to the clipboard.

    >>> 00000 (00:12:34.34) 01.png
    <<< 18086
    """
    frames = [
        f"{ts2f(ts=ts.group(1), fps=Fraction(fps))}"
        for screen in screens
        if (ts := search(r"(\d+:\d+:\d+\.\d+)", screen.stem))
    ]
    bookmark = ", ".join(frames) + "\n"
    click.echo(bookmark)
    copy(bookmark)
