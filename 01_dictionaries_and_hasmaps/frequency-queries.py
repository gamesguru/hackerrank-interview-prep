#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    def reverse_put(e, i):
        new_value = store[e]
        old_value = new_value - i

        if e in reverse_store[old_value]:
            reverse_store[old_value].remove(e)
        if new_value in reverse_store:
            reverse_store[new_value].append(e)
        else:
            reverse_store[new_value] = list()

    store = dict()
    reverse_store = dict()
    has_expected_n = False

    result = list()
    for i, query in enumerate(queries):
        if not i % 1000:
            print(i)

        action, e = query
        if action == 1:
            if e in store:
                store[e] += 1
            else:
                store[e] = 1
            reverse_put(e, 1)
        elif action == 2:
            if e in store:
                if store[e] > 0:
                    store[e] -= 1
                else:
                    del store[e]
            reverse_put(e, -1)
        else:  # action == 3
            # has_expected_n = int(bool([k for k, v in store.items() if v == e]))
            has_expected_n = e in reverse_store
            result.append(has_expected_n)
    # print('\n'.join(str(x) for x in result))
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
