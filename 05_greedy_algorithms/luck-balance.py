#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    # print('k', k)
    # print(contests)

    luck = 0.0

    # allow to lose ALL "unimportant" contests
    for con in contests:
        if con[1] == 0:
            luck += con[0]

    contests_important_sorted = sorted((x for x in contests if x[1] == 1), reverse=True)

    # greedily take (for losing) largest k "important" contests
    try:
        for i in range(k):
            luck += contests_important_sorted[i][0]
    except IndexError:
        pass

    # deduct luck for all won (n - k) "important" contests
    try:
        for i in range(k, len(contests_important_sorted)):
            luck -= contests_important_sorted[i][0]
    except IndexError:
        pass

    return int(luck)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # first_multiple_input = input().rstrip().split()

    # NOTE: expect 494906
    with open("luck-balance.txt", "r", encoding="utf-8") as _file:
        lines = [x.rstrip() for x in _file.readlines()]

    # print(lines)

    n = int(lines[0][0])
    k = int(lines[0][1])

    # k = 3
    # contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

    contests = []
    for i in range(1, len(lines)):
        val1 = lines[i].split()[0]
        val2 = lines[i].split()[1]
        contests.append((int(val1), int(val2)))

    result = luckBalance(k, contests)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
