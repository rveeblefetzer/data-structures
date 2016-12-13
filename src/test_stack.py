"""Tests for push and pop methods on Class stack."""

import pytest


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
