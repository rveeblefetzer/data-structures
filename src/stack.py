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
        return self._stack.pop()

    def _size(self):
        """Return the size of the stack."""
        return self._stack._size

    def _is_empty(self):
        """Return true if stack is empty."""
        if self._stack._size > 0:
            return False
        else:
            return True

    def __len__(self):
        """Set length to value of size."""
        return self._size()
