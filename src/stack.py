"""Implemetation of a stack data structure."""

from linked_list import LinkedList


class Stack(object):
    """Class to represent stack data structure."""

    def __init__(self, iterable=None):
        """Initialize a stack as a instance of a LinkedList."""
        self._stack = LinkedList(iterable)

    def push(self, val):
        """Add a value to the top of the stack."""
        self._stack.push(val)

    def pop(self):
        """Remove the head from the LinkedList and return that value."""
        self._stack.pop()
