#!/usr/bin/env python
import click

from .chapt2bmqpyml import chapt2bmqpyml
from .frames_denum import frames_denum
from .mpls2chap import mpls2chap
from .num_frames import num_frames
from .re_chapters import re_chapters
from .re_titles import re_titles
from .screens2bm import screens2bm
from .vs_screens import vs_screens
from .zones_validator import zones_validator


@click.group(
    context_settings={
        "show_default": True,
        "help_option_names": ["-h", "--help"],
    }
)
@click.version_option()
def cli() -> None:
    pass


cli.add_command(chapt2bmqpyml)
cli.add_command(frames_denum)
cli.add_command(mpls2chap)
cli.add_command(num_frames)
cli.add_command(re_chapters)
cli.add_command(re_titles)
cli.add_command(screens2bm)
cli.add_command(vs_screens)
cli.add_command(zones_validator)

if __name__ == "__main__":
    cli()
