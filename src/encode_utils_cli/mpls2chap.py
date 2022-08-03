#!/usr/bin/env python
from pathlib import Path

import click

from .util.load_mpls import load_mpls
from .util.timeconv import seconds2ts


@click.command()
@click.argument(
    "mpls",
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "-s",
    "--start-ep",
    type=int,
    default=1,
    help="Number of first episode in mpls",
)
def mpls2chap(mpls: Path, start_ep: int) -> None:
    """
    Make .txt chapters from .mpls
    """
    with mpls.open("rb") as data:
        chapterdata = load_mpls(data)[:-1]

    for number, ep in enumerate(chapterdata, start=start_ep):
        startpos = ep.times[0]
        chapters = [
            f"CHAPTER{index:02d}={seconds2ts((time - startpos) / 45000.0)}\n"
            f"CHAPTER{index:02d}NAME="
            for index, time in enumerate(ep.times)
        ]
        Path(f"{mpls.parent}/e{number}.txt").write_text("\n".join(chapters))
