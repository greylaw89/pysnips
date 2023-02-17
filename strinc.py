from collections import namedtuple
import os

from strincseps import Incrementor, dash, underscore, parens


def find_inc(str_: str, incs: list = [dash, underscore, parens]) -> Incrementor:
    """Find the appropriate Incrementor for a given string, if it already has a number at the end."""
    for inc in incs:
        if inc.rx.findall(str_):
            return inc
        continue
    return None


def find_inc_values(str_: str, inc: Incrementor) -> tuple:
    """Finds the starting position for new increments."""
    rr = inc.rx.findall(str_)
    if not len(rr) == 1:
        raise ValueError()
    rr = rr[0]
    if not len(rr) == 2:
        raise ValueError()
    cnum, num = rr
    num = int(num)
    return (cnum, num)


def inc_str(str_: str) -> str:
    """
    Increments a base string. String must already have a number seperated by a defined Incrementor at the end.
    e.g. test-1 -> test-2 or test_2 -> test_3
    """
    inc = find_inc(str_)
    c, n = find_inc_values(str_, inc)
    cidx = str_.rfind(c)
    str_ = str_[:cidx]
    str_ += inc.fmtstr.format(i = n + 1)
    return str_


def base_str_inc(base_: str, start: int = 1, inc: Incrementor = dash) -> str:
    """Creates a basic incrementor generator off a base string."""
    current = start
    while True:
        yield base_ + inc.fmtstr.format(i = current)
        current += 1
        continue
    return None


def filename_inc(filename: str, start: int = 1, inc: Incrementor = dash) -> str:
    """Generates a filename incremeter."""
    current = start - 1
    base_, ext = os.path.splitext(filename)
    def func():
        nonlocal current
        current += 1
        return base_ + inc.fmtstr.format(i = current) + ext
    return func
