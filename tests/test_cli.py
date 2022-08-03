#!/usr/bin/env python
from click.testing import CliRunner

from src.encode_utils_cli.__main__ import cli


def test_cli():
    runner = CliRunner()
    assert runner.invoke(cli, ["--help"]).exit_code == 0
    assert (
        runner.invoke(cli, ["frames-denum", "16886", "26280", "--denum", "2"]).output
        == "8443 13140\n"
    )
    assert (
        runner.invoke(cli, ["frames-denum", "16886", "26280", "--denum", "0.5"]).output
        == "33772 52560\n"
    )
