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
        if isinstance(head, list):
            node = Node(head[0])
            self.head = node
            for i in range(1, len(head)):
                self.push(head[i])
        else:
            self.head = head

    def push(self, val):
        """Push elements into list."""
        node = Node(val)
        node.next = self.head
        self.head = node

    def pop(self):
        """Remove head element and return value."""
        temp_data = self.head.data
        self.head = self.head.next
        return temp_data

    def size(self):
        """Return length of list."""
        count = 0
        current = self.head
        if self.head is None:
            return 0
        while current.next is not None:
            count += 1
            current = current.next
        return count + 1

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
