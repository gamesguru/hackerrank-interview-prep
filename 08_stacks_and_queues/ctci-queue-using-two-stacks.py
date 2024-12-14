#!/usr/bin/env python3
"""Two stack queue problem"""


class MyQueue:
    def __init__(self):
        pass

    def peek(self):
        pass

    def pop(self):
        pass

    def put(self, value):
        pass


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
