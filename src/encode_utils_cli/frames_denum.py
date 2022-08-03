#!/usr/bin/env python
import click
from pyperclip import copy


@click.command()
@click.argument("frames", nargs=-1, required=True, type=int)
@click.option("-d", "--denum", type=float, default=2)
def frames_denum(frames: tuple[int], denum: float) -> None:
    """
    Sort frames and divide without remainder by the specified divisor.
    The result will be copied to the clipboard.

    \b
    >>> frames_denum((16886, 26280), denum=2)
    <<< "8443 13140"
    >>> frames_denum((16886, 26280), denum=.5)
    <<< "33772 52560"
    """
    divided = " ".join(f"{int(frame // denum)}" for frame in sorted(frames, key=int))

    click.echo(divided)
    copy(divided)
