"""Test for singly linked list from link_list.py."""


def test_node_init_data():
    """Test that Node constructor works."""
    from linked_list import Node
    temp = Node(2)
    assert temp.data == 2


def test_node_init_next_none():
    """Test that Node constructor works with empty next."""
    from linked_list import Node
    temp = Node(2)
    assert temp.next is None


def test_node_init_next_node():
    """Test that Node constructor works with non empty next."""
    from linked_list import Node
    temp = Node(2)
    temp2 = Node(1, temp)
    assert temp2.next == temp


def test_linked_list_init_none():
    """Test that link_list initializes empty."""
    from linked_list import LinkedList
    temp = LinkedList()
    assert temp.head is None


def test_linked_list_init_node():
    """Test that link_list initializes empty."""
    from linked_list import LinkedList, Node
    # from linked_list import Node
    node = Node(2)
    temp = LinkedList(node)
    assert temp.head == node


def test_push_to_empty_list():
    """Test that a new node can be added to an empty list."""
    from linked_list import LinkedList, Node
    test_list = LinkedList()
    node = Node(2)
    test_list.push(node)
    assert test_list.head == node


