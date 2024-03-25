#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    m_dict = {}
    for m_word in magazine:
        if m_word not in m_dict:
            m_dict[m_word] = 1
        else:
            m_dict[m_word] += 1
        # if m_word == 'cpzso':
        #     print(f'M count: {m_dict[m_word]}')

    n_dict = {}
    for n_word in note:
        if n_word not in n_dict:
            n_dict[n_word] = 1
        else:
            n_dict[n_word] += 1
        # if n_word == 'cpzso':
        #     print(f'N count: {n_dict[n_word]}')

    for n_word in n_dict:
        if n_word not in m_dict or n_dict[n_word] > m_dict[n_word]:
            # print(n_word)
            # print(n_dict[n_word])
            # print(m_dict[n_word])
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
