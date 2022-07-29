#!/usr/bin/env python
from pathlib import Path

from vapoursynth import VideoNode, core


def source(video: Path) -> VideoNode:
    return (
        core.lsmas.LibavSMASHSource(source=video)
        if video.suffix == ".mp4"
        else core.lsmas.LWLibavSource(source=video)
    )
