#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    set1 = set(x for x in s1)
    set2 = set(x for x in s2)
    for c in set1:
        if c in set2:
            return 'YES'
    # print(set1)
    return 'NO'

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
