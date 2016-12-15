"""Implementation of linked lists.

This module makes two classes, Node and LinkedList, to manage linked lists.
A populated list will have a head and tail, and each node points to the node
following it, except for head nodes. Written by Marc Fieser and Rick Valenzuela
at Code Fellows' 401 Advanced Python class, Seattle, December 2016.
"""


class Node(object):
    """Create class to represent individual elements in data structure."""

    def __init__(self, data, next=None):
        """Something."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Implementation of linked lists.

    Methods:

    push(val) -
        Will insert the value val at the head of the list

    pop() -
        Will pop the first value off the head of the list and return it.

    size() -
        Returns number of nodes in list.

    search(val) -
        Return node with value of parameter val.

    remove(val)  -
        Will remove the first instance of val found in the list,
        starting from the head. If val is not present, it will raise
        an appropriate Python exception.

    display() -
        Prints all elements in list.
    """

    def __init__(self, iterable=None):
        """Instantiate LinkedList object, default empty or take iterable."""
        self.head = None
        self._size = 0
        if iterable:
            try:
                for value in iterable:
                    self.push(value)
            except:
                raise TypeError("Not an iterable")

    def push(self, val):
        """Push elements into list."""
        node = Node(val)
        node.next = self.head
        self.head = node
        self._size += 1

    def pop(self):
        """Remove head element and return value."""
        if self.head is None:
            raise IndexError("Cannot pop from empty.")
        temp_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp_data

    def size(self):
        """Return length of list."""
        return self._size

    def search(self, val):
        """Return node with data value of val."""
        current = self.head
        while current is not None:
            if current.data == val:
                return current
            current = current.next
        return None

    def remove(self, node):
        """Remove given node from list."""
        current = self.head
        if current.data == node.data:
            self.head = current.next
            return True
        while current.next is not None:
            if current.next.data == node.data:
                current.next = current.next.next
                return True
            current = current.next
        raise ValueError("Node not in list.")

    def display(self):
        """Display all elements in a linked list."""
        current = self.head
        result = "("
        while current is not None:
            if isinstance(current.data, str):
                result = result + "'" + current.data + "'"
            else:
                result = result + str(current.data)
            if current.next is not None:
                result += ", "
            current = current.next
        result += ')'
        return result

    def __len__(self):
        """Set length to value of size."""
        return self.size()

    def __repr__(self):
        """Call self.display when accessing __repr__."""
        return self.display()
