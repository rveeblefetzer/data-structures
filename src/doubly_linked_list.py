# -*- coding: utf-8 -*-
"""Implementation of a doubly-linked list.

A populated list will have a head and tail, and each node
points to nodes before and after (except for head and tail nodes).

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
        self._size -= 1

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

    def _size(self):
        """Return length of dll."""
        return self._size

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.head is None:
            raise IndexError("Cannot pop from empty.")
        self.head.before.after = None
        self.head.before = self.head

    def shift(self):
        """Remove the last value from the tail of the list and return it."""
        pass

    def remove(self, val):
        """Will remove the first instance of val found in the list."""
        pass
