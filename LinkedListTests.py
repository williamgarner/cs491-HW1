import io
import unittest
import unittest.mock
from LinkedList import LinkedList


class ListTest(unittest.TestCase):
	"""This class will test all functions, branches, and conditions in LinkedList
		The only function it will not test is print_list
	"""

	def test_empty_list(self):
		"""Statement coverage and Edge Coverage"""
		self.assertTrue(LinkedList().is_empty())

	def test_not_empty_list(self):
		"""Statement coverage"""
		list = LinkedList()
		list.push(1)
		self.assertEqual(list.is_empty(), False)

	def test_get_head(self):
		"""Statement coverage and function coverage"""
		list = LinkedList()
		list.push(2)
		self.assertEqual(list.get_head(), 2)

	def test_no_head(self):
		"""Statement coverage and edge"""
		self.assertEqual(LinkedList().get_head(), None)

	def test_get_all_data(self):
		"""Statement coverage"""
		list = LinkedList()
		list.push(1)
		list.push(2)
		list.push(3)

		self.assertEqual(list.get_all_data(), [3, 2, 1])

	def test_head_delete(self):
		"""Statement coverage and condition and edge"""
		list = LinkedList()
		list.push(1)
		self.assertTrue(list.delete_node(1))

	def test_delete_not_head(self):
		"""Statement coverage"""
		list = LinkedList()
		list.push(1)
		list.push(2)
		list.push(3)
		self.assertTrue(list.delete_node(2))

	def test_delete_no_head(self):
		"""Edge coverage"""
		self.assertFalse(LinkedList().delete_node(1))

	def test_delete_fail(self):
		"""Branch and condition coverage"""
		list = LinkedList()
		list.push(1)
		list.push(2)
		list.push(3)

		self.assertFalse(list.delete_node(4))


if __name__ == '__main__':
	unittest.main()
