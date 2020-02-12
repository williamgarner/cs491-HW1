import unittest

from Queue import Queue


class QueueTest(unittest.TestCase):
	"""This class will test all the functions in Queue"""
	def test_empty_queue(self):
		"""Statement and function and empty coverage"""
		self.assertTrue(Queue().is_empty())

	def test_not_empty_queue(self):
		"""Statement and function coverage"""
		queue = Queue()
		queue.enqueue(1)
		self.assertFalse(queue.is_empty())

	def test_dequeue(self):
		"""Statement and function coverage"""
		queue = Queue()
		queue.enqueue(1)
		self.assertEqual(queue.dequeue(), 1)

	def test_size_zero(self):
		"""Statement and function and edge coverage"""
		self.assertEqual(Queue().size(), 0)

	def test_size_not_zero(self):
		"""Statement and function coverage"""
		queue = Queue()
		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)

		self.assertEqual(queue.size(), 3)


if __name__ == '__main__':
	unittest.main()
