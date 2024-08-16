from pathlib import Path

import pytest
from click.testing import CliRunner

from encode_utils_cli.__main__ import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_help(runner: CliRunner):
    assert runner.invoke(cli, ["--help"]).exit_code == 0


def test_frames_denum(runner: CliRunner):
    assert (
        runner.invoke(cli, ["frames-denum", "16886", "26280", "--denum", "2"]).output
        == "8443 13140\n"
    )
    assert (
        runner.invoke(cli, ["frames-denum", "16886", "26280", "--denum", "0.5"]).output
        == "33772 52560\n"
    )


def test_re_titles(runner: CliRunner):
    assert (
        runner.invoke(cli, ["re-titles", "-c", "tests/resources/titles.toml"]).output
        == "e1: EP1 «The Prince`s New Clothes»\ne2: EP2 «The Prince and Kage»\ne3: EP3 «The New King»\ne4: EP4 «His First Journey»\ne5: EP5 «Intertwining Plots»\ne6: EP6 «The King of the Underworld»\ne7: EP7 «The Prince`s Apprenticeship»\ne8: EP8 «The Sacrifice of Dreams»\ne9: EP9 «The Queen and the Shield»\n\nop1: OP1 «Boy»\nop2: OP2 «Hadaka no Yuusha»\ned1: ED1 «Oz.»\ned2: ED2 «Flare»\n\n"
    )


def test_screens2bm(runner: CliRunner):
    assert (
        runner.invoke(
            cli,
            [
                "screens2bm",
                "tests/resources/00000 (00_00_03.34) 01.png",
                "tests/resources/00000 (00_12_34.34) 02.png",
            ],
        ).output
        == "80, 18086\n\n"
    )


def test_zones_validator(runner: CliRunner):
    assert runner.invoke(cli, ["zones-validator", "tests/resources/zones.yml"]).output == ""
    assert (
        runner.invoke(cli, ["zones-validator", "tests/resources/zones_broken.yml"]).output
        == "e2: 4173,6329,b=0.50/31888,34045,b=0.70/32158,b=0.39/33764,b=0.42/34046,34117,b=0.50 <- ['32158,b=0.39', '33764,b=0.42']\n"
    )


def test_mpls2chap(runner: CliRunner, tmp_path):
    assert (
        runner.invoke(
            cli, ["mpls2chap", "tests/resources/00000.mpls", "-s", "4", "-d", tmp_path]
        ).exit_code
        == 0
    )
    assert (
        Path(f"{tmp_path}/e4.txt").read_text() + "\n" == Path("tests/resources/e4.txt").read_text()
    )
