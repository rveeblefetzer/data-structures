"""Tests for push and pop methods on Class stack."""

import pytest

ITER_TABLE = [
    ['string', "('g', 'n', 'i', 'r', 't', 's')"],
    [[1, 2, 3], "(3, 2, 1)"],
    [(1, 2, 3), "(3, 2, 1)"],
]


@pytest.fixture
def test_stack():
    """Create test stack for testing stack functionality."""
    from stack import Stack
    test_stack = Stack()
    return test_stack


def test_init_stack(test_stack):
    """Test that stack is initialized."""
    assert test_stack._stack.head is None


def test_push_to_empty_stack(test_stack):
    """Test that push works on empty stack."""
    test_stack.push('phone')
    assert test_stack._stack.head.data == 'phone'


def test_push_to_non_empty_stack(test_stack):
    """Test pushing to populated stack."""
    test_stack.push(4)
    test_stack.push(5)
    assert test_stack._stack.head.next.data == 4


@pytest.mark.parametrize("iterable, result", ITER_TABLE)
def test_init_stack_w_iterables(iterable, result):
    """Test that a stack can init with iterable."""
    from stack import Stack
    test_stack = Stack(iterable)
    assert test_stack._stack.display() == result


def test_popping_empty_list(test_stack):
    """Test pop method on empty list."""
    with pytest.raises(IndexError):
        test_stack.pop()


def test_popping_populated_list(test_stack):
    """Test popping a list with nodes/values."""
    test_stack.push(4)
    test_stack.pop()
    assert test_stack._stack.head is None


def test_pop_returns_value(test_stack):
    """Test pop returns proper value."""
    test_stack.push(4)
    popped_value = test_stack.pop()
    assert popped_value == 4


def test_stack_size_of_empty(test_stack):
    """Test empty stack size is 0."""
    assert test_stack._size() == 0


def test_stack_size_of_non_empty(test_stack):
    """Test empty stack size is 0."""
    test_stack.push(5)
    assert test_stack._size() == 1


def test_is_empty_of_empty(test_stack):
    """Test stack is empty."""
    assert test_stack._is_empty()


def test_is_empty_of_populated_stack(test_stack):
    """Test stack is not empty."""
    test_stack.push(4)
    assert test_stack._is_empty() is False


def test_len_of_stack(test_stack):
    """Test len function."""
    assert len(test_stack) == 0
