#!/usr/bin/env python
from pathlib import Path

import click
from schema import Regex, Schema, SchemaError


@click.command()
@click.argument(
    "zones_config",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
def zones_validator(zones_config: Path) -> None:
    """
    Validate x265 zones.
    """
    text = zones_config.read_text()

    error_lines = []
    for line in text.split("\n"):
        if line and not line.isspace() and not line.lstrip().startswith("#"):
            try:
                for zone in line.split(": ")[1].split("/"):
                    Schema(Regex(r"^\d+,\d+,b=\d\.\d+$")).validate(zone)
            except SchemaError:
                error_lines.append(line)

    if error_lines:
        click.echo("validate_errors:")
        for line in error_lines:
            click.echo(line.replace("\n", ""))
