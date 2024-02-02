from fractions import Fraction

from encode_utils_cli.util.timeconv import seconds2f, seconds2ts, ts2f, ts2seconds


def test_timeconv():
    assert seconds2f(101, fps=Fraction("24000/1001")) == 2422
    assert seconds2ts(101) == "00:01:41.000"
    assert ts2f("00:01:41.000", fps=Fraction("24000/1001")) == 2422
    assert ts2seconds("00:01:41.000") == 101
