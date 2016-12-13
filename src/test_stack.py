"""Tests for push and pop methods on Class stack."""

import pytest

@pytest.fixture
def new_stack():
    from stack import stack
    test_stack = Stack()


def test_init_stack(test_stack):
    """Test that stack is initialized."""
    assert test_stack.data is None
