"""Entrypoint for cli."""

import click

from encode_utils_cli.chapt2bmqpyml import chapt2bmqpyml
from encode_utils_cli.frames_denum import frames_denum
from encode_utils_cli.mpls2chap import mpls2chap
from encode_utils_cli.num_frames import num_frames
from encode_utils_cli.re_chapters import re_chapters
from encode_utils_cli.re_titles import re_titles
from encode_utils_cli.screens2bm import screens2bm
from encode_utils_cli.vs_screens import vs_screens
from encode_utils_cli.zones_validator import zones_validator


@click.group(context_settings={"max_content_width": 120, "show_default": True})
@click.version_option()
def cli() -> None:
    """Entrypoint for cli."""


cli.add_command(chapt2bmqpyml)
cli.add_command(frames_denum)
cli.add_command(mpls2chap)
cli.add_command(num_frames)
cli.add_command(re_chapters)
cli.add_command(re_titles)
cli.add_command(screens2bm)
cli.add_command(vs_screens)
cli.add_command(zones_validator)
