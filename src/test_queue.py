"""Testing for Queue Class."""

import pytest


@pytest.fixture
def empty_queue():
    """Fixture for empty queue."""
    from queue import Queue
    queue = Queue()
    return queue


@pytest.fixture
def one_elem_queue(empty_queue):
    """Fixture for single node queue."""
    empty_queue.enqueue('Seattle')
    return empty_queue


@pytest.fixture
def two_elem_queue(one_elem_queue):
    """Fixture for two-node, populated dll."""
    one_elem_queue.enqueue(5)
    return one_elem_queue


@pytest.fixture
def three_elem_queue(two_elem_queue):
    """Fixture for three-node queue."""
    two_elem_queue.enqueue(7)
    return two_elem_queue


# node tests

def test_queue_exists_and_empty(empty_queue):
    """Test that node data is none after initialization."""
    assert empty_queue._queue.head.data is None


def test_queue_has_no_head(empty_queue):
    """Test that initialized queue has no head."""
    empty_queue.enqueue("Seattle")
    assert empty_queue._queue.head.data == "Seattle"
