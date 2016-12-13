"""Create a class for linked lists and a few methods to manipulate it."""


class Node(object):
    """Create class to represent individual elements in data structure."""

    def __init__(self, data, next=None):
        """Something."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Create linked lists."""

    def __init__(self, iterable=None):
        """Instantiate objects wi."""
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
        # import pdb; pdb.set_trace()
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
        print(result)
        return result
