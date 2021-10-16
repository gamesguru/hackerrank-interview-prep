#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    store = dict()
    result = list()
    for query in queries:
        action, e = query
        if action == 1:
            if e in store:
                store[e] += 1
            else:
                store[e] = 1
        elif action == 2:
            if e in store:
                store[e] -= 1
        else:  # action == 3
            has_expected_n = int(bool([k for k, v in store.items() if v == e]))
            result.append(has_expected_n)
    # print(result)
    return result


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    # fptr.write("\n".join(map(str, ans)))
    # fptr.write("\n")

    # fptr.close()
