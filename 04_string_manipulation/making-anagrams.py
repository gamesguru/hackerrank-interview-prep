#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def makeAnagram(a, b):
    # Gather letter counts into dictionary: 'char' --> n_occurrences
    letters_a = {}
    letters_b = {}

    for letter in a:
        if letter not in letters_a:
            letters_a[letter] = 1
        else:
            letters_a[letter] += 1

    for letter in b:
        if letter not in letters_b:
            letters_b[letter] = 1
        else:
            letters_b[letter] += 1

    # DEBUG
    # print(letters_a)
    # print(letters_b)

    # Start counting the number of deletions needed
    n_deletions = 0

    # Remove disjoint letters
    for letter in letters_a:
        if letter not in letters_b:
            n_deletions += letters_a[letter]

    for letter in letters_b:
        if letter not in letters_a:
            n_deletions += letters_b[letter]

    # Equalize excess/deficits of intersected letters
    for letter in set(letters_a).intersection(letters_b):
        # DEBUG
        # print('common letter', letter)
        n_deletions += math.fabs(letters_a[letter] - letters_b[letter])

    return int(n_deletions)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = input()
    # b = input()
    a = "cde"
    b = "abc"

    res = makeAnagram(a, b)
    print(res)

    # fptr.write(str(res) + '\n')
    # fptr.close()
