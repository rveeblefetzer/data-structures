"""Implemetation of a queue data structure.

This module makes a class Queue to manage a queue-style data structure.
It references the Dll class from the doubly_linked_list module. Elements
can be queued and dequeued to and from the end of the stack. Written by
Marc Fieser and Rick Valenzuela at Code Fellows' 401 Advanced Python class,
Seattle, December 2016.
"""


from doubly_linked_list import Dll


class Queue():
    """Class to represent the queue data structure.

    Methods:

    enqueue(val) -
        Add the value val to the tail of the queue.

    dequeue() -
        Remove the head of the queue and return its value.

    peek() -
        Return the value of the head of the queue.

    size() -
        Return the size of the queue.
    """

    def __init__(self):
        """Initialize a queue."""
        self._queue = Dll()

    def enqueue(self, val):
        """Add a value to the tail of the queue."""
        self._queue.append(val)

    def dequeue(self):
        """Remove the head of the queue and return its value."""
        return self._queue.pop()

    def peek(self):
        """Return the value of the head of the queue."""
        if self._queue.head:
            return self._queue.head.data
        return None

    def size(self):
        """Return the size of the queue."""
        return self._queue._size
