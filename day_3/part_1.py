#!/usr/bin/env python3

import sys

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIORITIES = {CHARSET[i]: i + 1 for i in range(len(CHARSET))}

total = 0
for line in sys.stdin:
    combined = line.rstrip()
    first, second = combined[: len(combined) // 2], combined[len(combined) // 2 :]
    (common,) = set(first).intersection(set(second))
    total += PRIORITIES[common]
print(total)
