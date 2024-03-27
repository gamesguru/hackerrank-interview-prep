#!/bin/python3

import math
import os
import random
import re
import sys


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


def print_doubly_linked_list(
    node,
    sep,
):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
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


def sortedInsert(llist, data):
    node = llist

    while True:
        print("@", node.data)
        if node.next and node.next.data < data:
            node = node.next
            print("->", node.data)
            continue
        break

    print("end @", str(node.data))

    # middle
    #       _
    # a <-> b <-> c <-> d
    # a <-> b <-> e <-> c <-> d
    #       *************
    # start
    # _
    # a <-> b
    # e <-> a <-> b
    # *******
    # end
    #       _
    # a <-> b
    # a <-> b <-> e
    #       *******

    new_block = DoublyLinkedListNode(data)

    new_block.prev = node
    new_block.next = node.next

    node.next = new_block
    node = node.next
    if node:
        node.prev = new_block

    return llist


if __name__ == "__main__":
    t = 1

    for t_itr in range(t):
        llist = DoublyLinkedList()

        data = 1
        input_list = [2, 3, 4]
        # data = 5
        # input_list = [1, 3, 4, 10]

        print("insert", data)

        for llist_item in input_list:
            llist.insert_node(llist_item)

        print("PRINT LIST - BEFORE")
        print_doubly_linked_list(llist.head, " ")

        print("RUN INSERT ALGO...")
        llist1 = sortedInsert(llist.head, data)
        print("... DONE INSERTING!")

        print()
        print("PRINT LIST - AFTER")
        print_doubly_linked_list(llist1, " ")
