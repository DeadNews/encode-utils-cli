#!/usr/bin/env python
from io import SEEK_CUR
from struct import unpack
from typing import BinaryIO, NamedTuple


class PlayList(NamedTuple):
    name: str
    times: list[int]


def load_mpls(f: BinaryIO, fix_overlap: bool = True) -> list[PlayList]:
    """
    Parse blu-ray .mpls
    https://gist.github.com/dk00/0a0634c5666cf1b8ab9f

    >>> [
    >>>     PlayList(
    >>>         name="00014", times=[189000000, 194469213, 225901239, 249525465, 253620806]
    >>>     ),
    >>>     PlayList(
    >>>         name="00015", times=[189000000, 200779267, 223110326, 249510450, 253620806]
    >>>     ),
    >>> ]
    """

    def int_be(data: bytes) -> int:
        return {
            1: ord,
            2: lambda b: unpack(">H", b)[0],
            4: lambda b: unpack(">I", b)[0],
        }[len(data)](data)

    f.seek(8)
    addr_items, addr_marks = int_be(f.read(4)), int_be(f.read(4))
    f.seek(addr_items + 6)
    item_count = int_be(f.read(2))
    f.seek(2, SEEK_CUR)

    def read_item() -> PlayList:
        block_size = int_be(f.read(2))
        name = f.read(5).decode()
        f.seek(7, SEEK_CUR)
        times = [int_be(f.read(4)), int_be(f.read(4))]
        f.seek(block_size - 20, SEEK_CUR)
        return PlayList(name, times)

    items = [read_item() for _ in range(item_count)]

    f.seek(addr_marks + 4)
    mark_count = int_be(f.read(2))

    def read_mark() -> tuple[int, int]:
        f.seek(2, SEEK_CUR)
        index = int_be(f.read(2))
        time = int_be(f.read(4))
        f.seek(6, SEEK_CUR)
        return (index, time)

    for _ in range(mark_count):
        index, time = read_mark()
        if time > items[index].times[-2]:
            items[index].times.insert(-1, time)

    if fix_overlap:
        b = None
        for item in items:
            a, b = b, item.times
            if a and b[0] < a[-1] < b[-1]:
                a[-1] = b[0]
        if b is not None and len(b) > 1 and b[-1] - b[-2] < 90090:
            b.pop()

    return items
