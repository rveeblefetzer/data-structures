"""Implementation of a stack data structure.

This module makes a class Stack to manage a stack-style data structure.
It references a LinkedList class from the linked_list module. Nodes can be
pushed and popped to and from the top of the stack. Written by Marc Fieser
and Rick Valenzuela at Code Fellows' 401 Advanced Python class, Seattle,
December 2016.
"""

from linked_list import LinkedList


class Stack(object):
    """Class to represent stack data structure.

    Methods:

    push(val) -
        Insert the value val to the top of the stack.

    pop() -
        Pop the first value off the stack and return it.

    _size() -
        Return the number of elements in the stack.

    _is_empty() -
        Return whether the stack contains elements.

    """

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
