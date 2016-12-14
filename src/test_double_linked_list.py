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
    """Fixture for one node populated dll."""
    empty_dll.push(6)
    return empty_dll


@pytest.fixture
def pop_dll_2(pop_dll):
    """Fixture for one node populated dll."""
    pop_dll.push(5)
    return pop_dll

# node tests


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

# init tests


def test_dll_init_empty_head(empty_dll):
    """Test dll is initialized empty."""
    assert empty_dll.head is None


def test_dll_init_empty_size(empty_dll):
    """Test dll is initialized with empty size."""
    assert empty_dll._size is 0

# push tests


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


def test_push_to_populated_dll(pop_dll):
    """Test that push adds to the head of a populated dll."""
    pop_dll.push(5)
    assert pop_dll.head.data == 5


def test_push_to_populated_dll_before(pop_dll):
    """Test that push moves Nodes before head of a populated dll."""
    pop_dll.push(5)
    assert pop_dll.head.before.data == 6


def test_push_to_populated_dll_size(pop_dll):
    """Test that push to populated array increments size."""
    pop_dll.push(5)
    assert pop_dll._size == 2

# append tests


def test_append_to_empty_dll_head(empty_dll):
    """Test append to empty dll adds new node as head ."""
    empty_dll.append(6)
    assert empty_dll.head.data == 6


def test_append_to_empty_dll_tail(empty_dll):
    """Test push to empty dll adds new node as tail."""
    empty_dll.append(6)
    assert empty_dll.tail.data == 6


def test_append_to_empty_dll_size(empty_dll):
    """Test that append to empty dll returns size 1."""
    empty_dll.append(6)
    assert empty_dll._size == 1


def test_append_to_populated_dll(pop_dll):
    """Test that append adds to the tail of a populated dll."""
    pop_dll.append(5)
    assert pop_dll.tail.data == 5


def test_append_to_populated_dll_after(pop_dll):
    """Test that append moves Nodes after tail of a populated dll."""
    pop_dll.append(5)
    assert pop_dll.tail.after.data == 6


def test_append_to_populated_dll_size(pop_dll):
    """Test that append to populated dll returns size incremented by one."""
    pop_dll.append(6)
    assert pop_dll._size == 2

# pop tests


def test_pop_from_empty(empty_dll):
    """Test pop can't called on empty list."""
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_pop_from_list_of_one(pop_dll):
    """Test pop from list of one empties list."""
    pop_dll.pop()
    assert pop_dll.head is None and pop_dll.tail is None


def test_pop_from_list_greater_than_one(pop_dll_2):
    """Test pop from multiple-item list pops/reassigns head, returns val."""
    pop_dll_2.pop()
    assert pop_dll_2.head.data == 6


def test_pop_returns_value(pop_dll):
    """Test that pop returns value of head node."""
    assert pop_dll.pop() == 6

# shift() tests


def test_shift_from_empty(empty_dll):
    """Test shift can't be called on empty list."""
    with pytest.raises(IndexError):
        empty_dll.shift()


def test_shift_from_list_of_one(pop_dll):
    """Test shift from list of one empties list."""
    pop_dll.shift()
    assert pop_dll.head is None and pop_dll.tail is None


def test_shift_from_list_greater_than_one(pop_dll_2):
    """Test shift from multiple-item list reassigns tail, returns val."""
    pop_dll_2.shift()
    assert pop_dll_2.head.data == 5


def test_shift_returns_value(pop_dll):
    """Test that shift returns value of head node."""
    assert pop_dll.shift() == 6

