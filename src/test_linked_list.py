"""Test for singly linked list from link_list.py."""


def test_node_init_data():
    """Test that Node constructor works."""
    from linked_list import Node
    temp = Node(2)
    assert temp.data == 2


def test_node_init_next():
    """Test that Node constructor works."""
    from linked_list import Node
    temp = Node(2)
    assert temp.next == None
