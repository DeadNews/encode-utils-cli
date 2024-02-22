from pathlib import Path

import click
from schema import Regex, Schema


@click.command()
@click.argument(
    "zones_config",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
def zones_validator(zones_config: Path) -> None:
    """Validate x264/x265 zones configuration file."""
    text = zones_config.read_text()

    targe_lines = [
        line
        for line in text.splitlines()
        if line and not line.isspace() and not line.lstrip().startswith("#")
    ]

    for line in targe_lines:
        if error_zones := [
            zone
            for zone in line.split(": ")[1].split("/")
            if not Schema(Regex(r"^\d+,\d+,b=\d\.\d+$")).is_valid(zone)
        ]:
            click.echo(f"{line} <- {error_zones}")
