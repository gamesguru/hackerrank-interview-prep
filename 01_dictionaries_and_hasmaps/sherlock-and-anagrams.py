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
        return [st[i : i + n : 1] for i in range(k) if len(st[i : i + n : 1]) == n]

    n_anagrams = 0
    for i in range(1, len(s)):
        subs = substrings(s, i)
        # print(subs)
        subs = [{c: x.count(c) for c in x} for x in subs]
        n = len(subs)
        for i in range(n):
            sub1 = subs[i]
            for j in range(i + 1, n):
                sub2 = subs[j]
                if sub1 == sub2:
                    print(sub1)
                    n_anagrams += 1

        # print(subs)
        # print()
    return n_anagrams


if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result))
