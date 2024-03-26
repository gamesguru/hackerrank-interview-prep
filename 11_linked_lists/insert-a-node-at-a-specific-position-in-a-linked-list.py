#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    # A -> B -> C -> D
    # A -> B -> E -> C -> D
    #      ***********
    n = 1
    node = llist
    while n < position:
        node = node.next
        if not node:
            print("WARNING: ran to tail!")
            break
        print(str(node.data))
        n += 1

    new_block = SinglyLinkedListNode(data)
    new_block.next = node.next
    node.next = new_block
    return llist


if __name__ == "__main__":
    llist = SinglyLinkedList()
    input_list = [16, 13, 7]

    for llist_item in input_list:
        llist.insert_node(llist_item)

    data = 1
    position = 2

    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, " ")
