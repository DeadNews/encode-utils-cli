from pathlib import Path
from random import sample

import click
from vapoursynth import RGB24, VideoNode, core

from encode_utils_cli.util.source import source


@click.command()
@click.argument(
    "vids",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "-d",
    "--out-dir",
    type=click.Path(file_okay=False, path_type=Path),
    help="Custom out dir.",
)
@click.option("-f", "--frames", type=str, help='Frames. Format: "1 2 3".')
@click.option("-o", "--offset", type=int, default=0, help="Offset for clip.")
@click.option("-c", "--crop", type=int, default=0, help="CropRel args.")
@click.option("-p", "--drop-prop", is_flag=True, help="Delete frame prop.")
def vs_screens(
    vids: tuple[Path],
    out_dir: Path,
    frames: str,
    offset: int,
    crop: int,
    drop_prop: bool,
) -> None:
    """Generate screen frames from videos."""
    frames = frames or " ".join([f"{i}" for i in sample(range(100, 10000), k=5)])
    click.echo(f"Requesting frames: {frames!r}")

    for vid in vids:
        out_dir = Path(vid.parent) if out_dir is None else out_dir
        out_dir.mkdir(exist_ok=True)
        save_pattern = Path(f"{out_dir}/{vid.stem} %d.png")

        clip = open_clip(vid, drop_prop=drop_prop, offset=offset, crop=crop)
        writer = core.imwri.Write(clip, "png", save_pattern)

        for frame in frames.split():
            click.echo(f"Writing: '{save_pattern}' {frame}")
            writer.get_frame(int(frame))


def open_clip(video: Path, drop_prop: bool, offset: int, crop: int) -> VideoNode:
    """Prepare clip."""
    clip = source(video)
    sd_height = 576

    if drop_prop:
        clip = (
            clip.std.Setframe_prop(prop="_Matrix", delete=True)
            .std.Setframe_prop(prop="_Transfer", delete=True)
            .std.Setframe_prop(prop="_Primaries", delete=True)
        )
    clip = clip.resize.Spline36(
        format=RGB24,
        matrix_in_s="709" if clip.height >= sd_height else "601",
    )
    if offset:
        clip = clip.std.Trim(offset, clip.num_frames - 1)
    if crop:
        clip = clip.std.CropRel(top=crop, bottom=crop)

    return clip
