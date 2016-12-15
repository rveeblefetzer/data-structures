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
    one_elem_queue.enqueue("Bellingham")
    return one_elem_queue


def test_queue_exists_and_empty(empty_queue):
    """Test that node data is none after initialization."""
    assert empty_queue._queue.head is None


def test_queue_has_no_head(empty_queue):
    """Test that initialized queue has no head."""
    empty_queue.enqueue("Seattle")
    assert empty_queue._queue.head.data == "Seattle"


def test_enqueue_increments_size(one_elem_queue):
    """Test that enqueing elemnt increases queue length."""
    one_elem_queue.enqueue("Bellingham")
    assert one_elem_queue.size() == 2


def test_head_enqueuing_to_populated_list(one_elem_queue):
    """Test head in populated list doesn't change on enqueue."""
    one_elem_queue.enqueue("Tacoma")
    assert one_elem_queue._queue.head.data == "Seattle"
    assert one_elem_queue._queue.head.before.data == "Tacoma"


def test_dequeue_from_empty_queue(empty_queue):
    """Test that you can't dequeue an empty queue."""
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_dequeue_from_one_elem_list(one_elem_queue):
    """Test that dequeue on a queue of 1 empties queue."""
    one_elem_queue.dequeue()
    assert one_elem_queue._queue.head is None
    assert one_elem_queue.size() == 0


def test_head_on_dequeue_from_two_elem_list(two_elem_queue):
    """Test head element removed from queue and size adjusted."""
    two_elem_queue.dequeue()
    assert two_elem_queue._queue.head.data == "Bellingham"
    assert two_elem_queue.size() == 1


def test_peek_empty_queue(empty_queue):
    """Test that peek returns None."""
    assert empty_queue.peek() is None


def test_peek_queue_of_one(two_elem_queue):
    """Test that peek returns value."""
    assert two_elem_queue.peek() == 'Seattle'
    assert two_elem_queue._queue.head.data == "Seattle"


def test_size_queue_of_two(two_elem_queue):
    """Check size for queue of two."""
    assert two_elem_queue.size() == 2
