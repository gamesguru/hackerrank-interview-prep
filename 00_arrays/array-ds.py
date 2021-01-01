#!/bin/python3


# Complete the reverseArray function below.
def reverseArray(a):
    n = len(a) - 1
    for i in range(len(a) // 2):
        j = n - i
        a[i], a[j] = a[j], a[i]
    return a


if __name__ == "__main__":

    arr = [1, 3, 4, 2]

    res = reverseArray(arr)

    print(res)
