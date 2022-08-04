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
    assert (
        runner.invoke(cli, ["re-titles", "-c", "tests/test_files/titles.toml"]).output
        == "e1: EP1 «The Prince`s New Clothes»\ne2: EP2 «The Prince and Kage»\ne3: EP3 «The New King»\ne4: EP4 «His First Journey»\ne5: EP5 «Intertwining Plots»\ne6: EP6 «The King of the Underworld»\ne7: EP7 «The Prince`s Apprenticeship»\ne8: EP8 «The Sacrifice of Dreams»\ne9: EP9 «The Queen and the Shield»\n\nop1: OP1 «Boy»\nop2: OP2 «Hadaka no Yuusha»\ned1: ED1 «Oz.»\ned2: ED2 «Flare»\n\n"
    )
    assert (
        runner.invoke(
            cli,
            [
                "screens2bm",
                "tests/test_files/00000 (00:12:34.34) 01.png",
                "tests/test_files/00000 (00:14:14.34) 02.png",
            ],
        ).output
        == "18086, 20484\n\n"
    )
