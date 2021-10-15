#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    def substrings(st, n):
        k = len(st)
        return [st[i:i + n:1] for i in range(k) if len(st[i:i + n:1]) == n]

    # for i in range(1, len(s)):


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        # print(str(result))

