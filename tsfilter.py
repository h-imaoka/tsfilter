#!/usr/bin/env python3
import sys
import re
from datetime import datetime
from math import log10


def to_isoformat(m):
    ts = float(m[1])
    if ts - int(ts) == 0:
        ts = ts / 10**(int(log10(ts)) - 9)
    dt = datetime.fromtimestamp(ts)
    return m[0].replace(m[1], dt.isoformat())


def main():
    pattern = re.compile(r'(?:^|\D)(1[3-9]\d{8}[.]\d{3,6}|1[3-9]\d{8,14})')
    for line in sys.stdin:
        line = pattern.sub(to_isoformat, line)
        print(line, end='')


if __name__ == '__main__':
    main()
