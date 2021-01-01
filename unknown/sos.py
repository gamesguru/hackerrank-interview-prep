#!/bin/python3

# Complete the marsExploration function below.
def marsExploration(s):

    nums = [3 * i for i in range(len(s) // 3)]
    arr = [s[i : i + 3] for i in nums]

    n = 0
    for e in arr:
        # if e == "SOS":
        #     continue
        if e[0] != "S":
            n += 1
        if e[1] != "O":
            n += 1
        if e[2] != "S":
            n += 1
    return n


if __name__ == "__main__":

    s = "SOSSPSSQSSOR"

    result = marsExploration(s)
    print(result)
