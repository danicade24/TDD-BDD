from unittest import TestCase
from my_queue import Queue

class TestQueue(TestCase):
    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True
        queue.enqueue(1)
        assert queue.is_empty() is False

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.front() == 1
        queue.enqueue(2)
        assert queue.front() == 1  # El primer elemento permanece al frente

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.front() == 2
        queue.dequeue()
        assert queue.is_empty() is True

    def test_front(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.front() == 1
        queue.enqueue(2)
        assert queue.front() == 1  # El primer elemento sigue siendo el frente
