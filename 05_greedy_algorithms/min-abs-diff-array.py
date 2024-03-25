#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr):
    n = len(arr)

    # sort array
    arr.sort()

    d = -1
    for i in range(n - 1):
        _d = int(math.fabs(arr[i] - arr[i + 1]))
        if _d < d or d == -1:
            d = _d

    return d


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))

    n = 3
    arr = [3, -7, 0]

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
