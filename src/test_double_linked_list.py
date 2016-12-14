"""Test for double_linked_list from doubly_link_list.py."""

import pytest


@pytest.fixture
def empty_dll():
    """Fixture for empty doubly linked list."""
    from doubly_linked_list import Dll
    dll = Dll()
    return dll


@pytest.fixture
def pop_dll(empty_dll):
    empty_dll.push(6)
    return empty_dll


def test_node_exists_and_empty():
    """Test that node data is none after initialization."""
    from doubly_linked_list import Node
    node = Node()
    assert node.data is None


def test_node_exists_with_value():
    """Test that node data has value after initialization."""
    from doubly_linked_list import Node
    node = Node(6)
    assert node.data is 6


def test_node_before_is_none():
    """Test that node data has value after initialization."""
    from doubly_linked_list import Node
    node = Node(6)
    assert node.before is None


def test_node_after_is_none():
    """Test that node data has value after initialization."""
    from doubly_linked_list import Node
    node = Node(6)
    assert node.after is None


def test_dll_init_empty_head(empty_dll):
    """Test dll is initialized empty."""
    assert empty_dll.head is None


def test_dll_init_empty_head(empty_dll):
    """Test dll is initialized empty size."""
    assert empty_dll._size is 0


def test_push_to_empty_dll_head(empty_dll):
    """Test push to empty dll adds new node with head."""
    empty_dll.push(6)
    assert empty_dll.head.data == 6


def test_push_to_empty_dll_tail(empty_dll):
    """Test push to empty dll adds new node with tail."""
    empty_dll.push(6)
    assert empty_dll.tail.data == 6


def test_push_to_empty_dll_size(empty_dll):
    """Test push to empty dll adds new node with head."""
    empty_dll.push(6)
    assert empty_dll._size == 1


def test_push_to_populated_array(pop_dll):
    """Test that push adds to the head of a populated dll."""
    pop_dll.push(5)
    assert pop_dll.head.data == 5


def test_push_to_populated_array_next(pop_dll):
    """Test that push moves Nodes before head of a populated dll."""
    pop_dll.push(5)
    assert pop_dll.head.before.data == 6


def test_append_to_empty_dll_head(empty_dll):
    """Test push to empty dll adds new node with head."""
    empty_dll.append(6)
    assert empty_dll.head.data == 6


def test_append_to_empty_dll_tail(empty_dll):
    """Test push to empty dll adds new node with tail."""
    empty_dll.append(6)
    assert empty_dll.tail.data == 6


def test_append_to_populated_array(pop_dll):
    """Test that append adds to the tail of a populated dll."""
    pop_dll.append(5)
    assert pop_dll.tail.data == 5


def test_append_to_populated_array_next(pop_dll):
    """Test that append moves Nodes after tail of a populated dll."""
    pop_dll.append(5)
    assert pop_dll.tail.after.data == 6


