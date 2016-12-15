"""Implemetation of a queue data structure."""


from doubly_linked_list import Dll


class Queue():
    """Class to represent the queue data structure."""

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
        """Return the value of the head of hte queue."""
        if self._queue.head:
            return self._queue.head.data
        return None

    def size(self):
        """Return the size of the queue."""
        return self._queue._size
