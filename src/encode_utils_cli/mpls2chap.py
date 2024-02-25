from pathlib import Path

import click

from encode_utils_cli.util.load_mpls import load_mpls
from encode_utils_cli.util.timeconv import seconds2ts


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
    help="Number of first episode in mpls.",
)
@click.option(
    "-d",
    "--out-dir",
    type=click.Path(file_okay=False, path_type=Path),
    help="Custom out dir.",
)
def mpls2chap(mpls: Path, start_ep: int, out_dir: Path) -> None:
    """Convert MPLS file to chapter files."""
    out_dir = Path(mpls.parent) if out_dir is None else out_dir

    with mpls.open("rb") as data:
        chapterdata = load_mpls(data)[:-1]

    for number, ep in enumerate(chapterdata, start=start_ep):
        startpos = ep.times[0]
        chapters = [
            f"CHAPTER{index:02d}={seconds2ts((time - startpos) / 45000.0)}\n"
            f"CHAPTER{index:02d}NAME="
            for index, time in enumerate(ep.times)
        ]
        Path(f"{out_dir}/e{number}.txt").write_text("\n".join(chapters))
