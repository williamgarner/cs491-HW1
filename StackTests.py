import unittest

from Stack import Stack


class StackTest(unittest.TestCase):
	"""This class will test all of Stack except print_stack"""
	def test_empty(self):
		"""Statement and edge coverage"""
		self.assertTrue(Stack().is_empty())

	def test_not_empty(self):
		"""Statement and functional coverage"""
		stack = Stack()
		stack.push(1)

		self.assertFalse(stack.is_empty())

	def test_empty_pop(self):
		"""Edge and statement coverage"""
		self.assertFalse(Stack().pop())

	def test_pop(self):
		"""Statement and functional coverage"""
		stack = Stack()
		stack.push(1)
		stack.push(2)
		stack.push(3)

		self.assertTrue(stack.pop())

	def test_get_data(self):
		"""Statement and functional coverage"""
		stack = Stack()
		stack.push(1)
		stack.push(2)
		stack.push(3)

		self.assertEqual(stack.get_data(), [3,2,1])


if __name__ == '__main__':
	unittest.main()
