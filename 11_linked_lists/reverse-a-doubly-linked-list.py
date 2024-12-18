#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(_list: DoublyLinkedListNode):
    if _list is None: return None
    # head -> first <-> ... <-> last <- tail
    # first <-> second <-> ... <-> last -> NULL
    # ^ head                       ^ tail
    # 1. Swap head and tail
    # 2. Traverse whole list and swap prev and next

    while _list.next is not None:
        _list.next, _list.prev = _list.prev, _list.next
        _list = _list.prev
    _list.next, _list.prev = _list.prev, _list.next
    # Head Tail
    # head -> first -> second ->... -> last

    return _list


if __name__ == '__main__':
    fptr = sys.stdout
    sys.stdin = StringIO("""1
4
1
2
3
4
""")
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ', fptr)
