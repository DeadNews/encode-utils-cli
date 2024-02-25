from pathlib import Path

import click

from encode_utils_cli.util.source import source


@click.command()
@click.argument(
    "vids",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
def num_frames(vids: tuple[Path]) -> None:
    """Calculate the number of frames in the given videos."""
    for vid in vids:
        click.echo(f"{vid.stem}.num_frames: {source(vid).num_frames}")
