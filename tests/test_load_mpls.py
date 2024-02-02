from pathlib import Path

from encode_utils_cli.util.load_mpls import PlayList, load_mpls


def test_load_mpls():
    with Path("tests/resources/00000.mpls").open("rb") as data:
        assert load_mpls(data) == [
            PlayList(
                name="00000",
                times=[
                    189000000,
                    195486480,
                    199536776,
                    224606195,
                    249142582,
                    253189125,
                    189000000,
                ],
            ),
            PlayList(
                name="00001",
                times=[189000000, 193048419, 231045753, 265912460, 270005925],
            ),
            PlayList(
                name="00002",
                times=[
                    189000000,
                    192350221,
                    196453070,
                    212650501,
                    223947412,
                    238466917,
                    253525085,
                    257618550,
                ],
            ),
            PlayList(
                name="00011",
                times=[
                    189000000,
                    194645640,
                    198765380,
                    222344561,
                    247907598,
                    189000000,
                ],
            ),
            PlayList(
                name="00012",
                times=[189000000, 193140386, 220009728, 249608047, 253701511],
            ),
            PlayList(
                name="00013",
                times=[189000000, 193189185, 220096065, 249525465, 253620806],
            ),
            PlayList(
                name="00014",
                times=[189000000, 194469213, 225901239, 249525465, 253620806],
            ),
            PlayList(
                name="00015",
                times=[189000000, 200779267, 223110326, 249510450, 253620806],
            ),
        ]
