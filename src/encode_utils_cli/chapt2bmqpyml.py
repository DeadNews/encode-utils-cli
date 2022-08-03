#!/usr/bin/env python
from fractions import Fraction
from pathlib import Path
from re import findall, sub

import click
from yaml import dump

from .util.source import source
from .util.timeconv import ts2f


@click.command()
@click.argument(
    "episodes",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option("-f", "--fps", type=str, default="24000/1001")
@click.option(
    "-v",
    "--vid-info",
    is_flag=True,
    default=False,
    help="Get corresponding videos info",
)
@click.option(
    "-c",
    "--custom-layout",
    is_flag=True,
    default=False,
    help="Custom layout",
)
def chapt2bmqpyml(
    episodes: tuple[Path],
    fps: str,
    vid_info: bool,
    custom_layout: bool,
) -> None:
    """
    Convert chapters into yaml, corresponding bookmarks and qp files.
    """
    for ep in episodes:
        chapters = ep.read_text()

        clip = source(Path(f"{ep.parents[1]}/{ep.stem}.mp4")) if vid_info else None
        fps_ = Fraction(
            fps if clip is None else clip.fps.numerator / clip.fps.denominator
        )

        names = [
            sub(r"[ ,]", "_", name) for name in findall(r"NAME=([^\n]+)", chapters)
        ]
        frames = [ts2f(ts, fps_) for ts in findall(r"\d+=(\d+:\d+:\d+\.\d+)", chapters)]

        if custom_layout:
            bmk = Path(f"{ep.parents[2]}/{ep.stem}.vpy.bookmarks")
            qpf = Path(f"{ep.parents[2]}/in/{ep.stem}.qp")
            yml = Path(f"{ep.parents[2]}/chapters.yaml")
        else:
            bmk = Path(f"{ep.parent}/{ep.stem}.vpy.bookmarks")
            qpf = Path(f"{ep.parent}/{ep.stem}.qp")
            yml = Path(f"{ep.parent}/chapters.yaml")

        bmk.write_text(", ".join(f"{frame}" for frame in frames) + "\n")
        qpf.write_text("\n".join(f"{frame} I -1" for frame in frames))

        chap = {ep.stem: dict(zip(names, frames))}
        if clip is not None:
            chap[ep.stem]["EOF"] = clip.num_frames

        with yml.open("a") as stream:
            dump(data=chap, stream=stream, sort_keys=False)
