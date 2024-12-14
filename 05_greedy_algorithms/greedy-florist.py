#!/usr/bin/env
"""Greedy algorithm for florist flowers"""
from typing import List


def get_min_cost(k: int, c: List[int]) -> int:
    """Greedy algorithm"""
    cost = 0
    friend_purchase_count = [0] * k
    curr_friend = 0
    c.sort()
    while len(c) > 0:
        l = c.pop()
        cost += (1 + friend_purchase_count[curr_friend]) * l
        friend_purchase_count[curr_friend] += 1
        curr_friend = (curr_friend + 1) % len(friend_purchase_count)
    return cost


print(
    get_min_cost(
        k=3,
        # c=[2, 5, 6],
        # c=[1, 3, 5, 7, 9],
        c=[4, 2, 3, 1]
    )
)
