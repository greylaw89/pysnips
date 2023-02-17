from collections import namedtuple
import re


Incrementor = namedtuple("Incrementor", ["name", "rx", "fmtstr"])


dash = Incrementor("Dash", re.compile(r"(-\s?([0-9]+)\s?$)"), "-{i}")
underscore = Incrementor("Underscore", re.compile(r"(_\s?([0-9]+)\s?$)"), "_{i}")
parens = Incrementor("Parens", re.compile(r"(\(\s?([0-9]+)\s?\)$)"), "({i})")