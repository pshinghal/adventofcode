#!/usr/bin/env python3

import sys

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIORITIES = {CHARSET[i]: i + 1 for i in range(len(CHARSET))}

total = 0
group = []
for line in sys.stdin:
    group.append(line.rstrip())
    if len(group) == 3:
        (badge,) = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total += PRIORITIES[badge]
        group = []
print(total)
