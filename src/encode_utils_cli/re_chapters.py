#!/usr/bin/env python
from pathlib import Path
from re import findall, sub

import click
from yaml import safe_load


@click.command()
@click.argument(
    "episodes",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "-c",
    "--config",
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help=".yaml config",
)
def re_chapters(episodes: tuple[Path], config: Path) -> None:
    """
    Replace chapters names.
    """
    names = safe_load(config.read_text())

    for ep in episodes:
        chapters = ep.read_text()
        chap_count = len(findall(r"(NAME=)", chapters))
        zero_chap = findall(r"(CHAPTER00NAME=)", chapters)
        pad = 0 if zero_chap else 1

        for i in range(chap_count):
            chapters = sub_chapter(
                chapters=chapters,
                num=i + pad,
                name=names[chap_count][i],
            )

        ep.write_text(chapters)


def sub_chapter(chapters: str, num: int, name: str) -> str:
    """
    Replace chapter name.
    """
    return sub(rf"(CHAPTER{num:02d}NAME=)(.*)", rf"\1{name}", chapters)
