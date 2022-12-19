#!/usr/bin/env python3

import sys

cals = []
curr = 0
for line in sys.stdin:
    if line == '\n':
        cals.append(curr)
        curr = 0
    else:
        curr += int(line.rstrip())
cals.append(curr)

print(sum(sorted(cals)[-3:]))
