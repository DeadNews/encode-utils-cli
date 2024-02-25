from fractions import Fraction


def seconds2ts(s: float) -> str:
    """Convert seconds to timestamp in the format `hh:mm:ss.xxx`."""
    m = s // 60
    s %= 60
    h = m // 60
    m %= 60
    return f"{h:02.0f}:{m:02.0f}:{s:06.3f}"


def ts2seconds(ts: str) -> float:
    """Convert timestamp `hh:mm:ss.xxxx` to seconds."""
    h, m, s = map(float, ts.split(":"))
    return h * 3600 + m * 60 + s


def seconds2f(s: float, fps: Fraction) -> int:
    """Convert seconds to frames."""
    return round(s * fps)


def ts2f(ts: str, fps: Fraction) -> int:
    """Convert a timestamp `hh:mm:ss.xxxx` in number of frames."""
    return seconds2f(s=ts2seconds(ts), fps=fps)
