import click
from pyperclip import copy as clipboard_copy


@click.command()
@click.argument("frames", nargs=-1, required=True, type=int)
@click.option("-d", "--denum", type=float, default=2, help="Divisor.")
@click.option(
    "--copy/--no-copy",
    is_flag=True,
    default=True,
    help="Copy the result to the clipboard.",
)
def frames_denum(frames: tuple[int], denum: float, copy: bool) -> None:
    """Divide the frames by the specified divisor.

    \f
    Example:

        >>> frames_denum((16886, 26280), denum=2)
        <<< "8443 13140"
        >>> frames_denum((16886, 26280), denum=.5)
        <<< "33772 52560"
    """  # noqa: D301
    divided = " ".join(f"{int(frame // denum)}" for frame in sorted(frames, key=int))

    click.echo(divided)
    if copy:
        clipboard_copy(divided)
