"""Test for double_linked_list from doubly_link_list.py."""

import pytest


def test_node_exists_and_empty():
    """Test that node head is none after initialization."""
    from doubly_linked_list import Node
    node = Node()
    assert node.head is None
