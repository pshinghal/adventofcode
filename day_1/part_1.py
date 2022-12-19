#!/usr/bin/env python3

import sys

maxcal = 0
curr = 0
for line in sys.stdin:
    if line == '\n':
        curr = 0
    else:
        curr += int(line.rstrip())
        maxcal = max(maxcal, curr)
print(maxcal)
