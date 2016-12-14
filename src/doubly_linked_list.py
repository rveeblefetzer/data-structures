# -*- coding: utf-8 -*-
"""Implementation of a doubly-linked list."""


class Node(object):
<<<<<<< HEAD
    """Implementation of a Node for a doubly-linked list."""
=======
    u"""Implementation of a Node for a doubly-linked list."""
>>>>>>> 221401e7139001c96a1b08d267abfbf24fd21877

    def __init__(self, data=None, after=None, before=None):
        """Initialize Node instance."""
        self.data = data
        self.after = after
        self.before = before


class Dll(object):
    u"""Implementation for a doubly-linked-list.

    Methods :

    push(val) -
        Will insert the value ‘val’ at the head of the list

    append(val) -
        Will append the value ‘val’ at the tail of the list

    pop() -
        Will pop the first value off the head of the list and return it.

    shift() -
        Will remove the last value from the tail of the list and return it.

    remove(val)  -
        Will remove the first instance of ‘val’ found in the list,
        starting from the head. If ‘val’ is not present, it will raise
        an appropriate Python exception.
    """

    def __init__(self, head, tail):
        u"""Initialize a doubly-linked-list."""
        self.head = head
        self.tail = tail

    def push(self, val):
        u"""Will insert the value ‘val’ at the head of the list."""
        pass

    def append(self, val):
        u"""Will append the value ‘val’ at the tail of the list."""
        pass

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        pass

    def shift(self):
        """Remove the last value from the tail of the list and return it."""
        pass

    def remove(self, val):
        u"""Will remove the first instance of ‘val’ found in the list."""
        pass
