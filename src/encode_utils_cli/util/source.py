from pathlib import Path

from vapoursynth import VideoNode, core


def source(video: Path) -> VideoNode:
    """Load a video source using VapourSynth.

    Args:
        video: The path to the video file.

    Returns:
        VideoNode: The loaded video source.
    """
    return (
        core.lsmas.LibavSMASHSource(source=video)
        if video.suffix == ".mp4"
        else core.lsmas.LWLibavSource(source=video)
    )
