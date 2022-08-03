#!/usr/bin/env python
from pathlib import Path

import click

from .util.source import source


@click.command()
@click.argument(
    "vids",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
def num_frames(vids: tuple[Path]) -> None:
    """
    Print clip num frames.
    """
    for vid in vids:
        click.echo(f"{vid.stem}.num_frames: {source(vid).num_frames}")
