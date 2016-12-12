"""Create a class for linked lists and a few methods to manipulate it."""


class Node(object):
    """Create class to represent individual elements in data structure."""

    def __init__(self, data, next=None):
        """Something."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Create linked lists."""

    def __init__(self, head=None):
        """Instantiate objects with a head defaulted to None."""
        self.head = head

    def push(self, val):
        """Create push method."""
        node = Node(val)
        self.head = node
