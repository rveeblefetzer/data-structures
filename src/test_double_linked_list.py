"""Test for double_linked_list from doubly_link_list.py."""

import pytest


@pytest.fixture
def empty_dll():
    """Fixture for empty doubly linked list."""
    from doubly_linked_list import Dll
    dll = Dll()
    return dll


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


def test_push_to_empty_dll_head(empty_dll):
    """Test push to empty dll adds new node with head."""
    empty_dll.push(6)
    assert empty_dll.head.data == 6


def test_push_to_empty_dll_tail(empty_dll):
    """Test push to empty dll adds new node with tail."""
    empty_dll.push(6)
    assert empty_dll.tail.data == 6

