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
    node = Node(2)
    node2 = Node(1, node)
    assert node2.next == node


def test_linked_list_init_none():
    """Test that link_list initializes empty."""
    from linked_list import LinkedList
    test_list = LinkedList()
    assert test_list.head is None


def test_linked_list_init_node():
    """Test that link_list initializes empty."""
    from linked_list import LinkedList, Node
    # from linked_list import Node
    node = Node(2)
    test_list = LinkedList(node)
    assert test_list.head == node


def test_push_to_empty_list():
    """Test that a new node can be added to an empty list."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(7)
    assert test_list.head.data == 7


def test_push_to_nonempty_list_head():
    """Test that push adds to the front of a list."""
    from linked_list import LinkedList, Node
    node = Node(2)
    test_list = LinkedList(node)
    test_list.push(4)
    assert test_list.head.data == 4


def test_push_to_nonempty_list_next():
    """Test that push adds to the front of a list."""
    from linked_list import LinkedList, Node
    node = Node(2)
    test_list = LinkedList(node)
    test_list.push(4)
    assert test_list.head.next.data == 2


def test_pop_from_list():
    """Test that pop removes head from list."""
    from linked_list import LinkedList, Node
    node = Node(2)
    test_list = LinkedList(node)
    test_list.push(4)
    test_list.pop()
    assert test_list.head.data == 2


def test_pop_from_list_return_value():
    """Test that pop returns value of current head from list."""
    from linked_list import LinkedList, Node
    node = Node(2)
    test_list = LinkedList(node)
    test_list.push(4)
    assert test_list.pop() == 4
