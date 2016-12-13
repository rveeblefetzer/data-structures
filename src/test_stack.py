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
    from stack import Stack
    test_stack = Stack(iterable)
    assert test_stack._stack.display() == result


def test_popping_empty_list(test_stack):
    with pytest.raises(IndexError):
        test_stack.pop()
