# -*- coding: utf-8 -*-
"""Implementation of a doubly-linked list.

This module makes two classes, Node and Dll, to manage a two-way linked list.
 A populated list will have a head and tail, and each node points to nodes
before and after (except for head and tail nodes). Written by Marc Fieser
and Rick Valenzuela at Code Fellows' 401 Advanced Python class, Seattle,
December 2016.
"""


class Node(object):
    """Implementation of a Node for a doubly-linked list."""

    def __init__(self, data=None, after=None, before=None):
        """Initialize Node instance."""
        self.data = data
        self.after = after
        self.before = before


class Dll(object):
    """Implementation for a doubly-linked-list.

    Methods :

    push(val) -
        Will insert the value val at the head of the list

    append(val) -
        Will append the value val at the tail of the list

    pop() -
        Will pop the first value off the head of the list and return it.

    shift() -
        Will remove the last value from the tail of the list and return it.

    remove(val)  -
        Will remove the first instance of val found in the list,
        starting from the head. If val is not present, it will raise
        an appropriate Python exception.
    """

    def __init__(self):
        """Initialize a doubly-linked-list."""
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, val):
        """Will insert the value val at the head of the list."""
        node = Node(val)
        if self.head:
            node.before = self.head
            self.head.after = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self._size += 1

    def append(self, val):
        """Will append the value val at the tail of the list."""
        node = Node(val)
        if self.tail:
            node.after = self.tail
            self.tail.before = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self._size += 1

    def _get_size(self):
        """Return length of dll."""
        return self._size

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.head is None:
            raise IndexError("Cannot pop from empty.")
        temp_data = self.head.data
        if self._size == 1:
            self.head = None
            self.tail = None
        else:
            self.head.before.after = None
            self.head = self.head.before
        self._size -= 1
        return temp_data

    def shift(self):
        """Remove the last value from the tail of the list and return it."""
        if self.tail is None:
            raise IndexError("Cannot pop from empty.")
        temp_data = self.tail.data
        if self._size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.after.before = None
            self.tail = self.tail.after
        self._size -= 1
        return temp_data

    def remove(self, val):
        """Will remove the first instance of val found in the list."""
        if self.head is None:
            raise(IndexError)
        current = self.head
        found = False
        while current is not None:
            print(current.data)
            if current.data == val:
                self._size -= 1
                found = True
                if current.after is None:
                    self.head = current.before
                else:
                    current.after.before = current.before
                if current.before is None:
                    self.tail = current.after
                else:
                    current.before.after = current.after
            current = current.before
        if not found:
            raise(IndexError)
