class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if not self.is_empty():
			self.stack.pop()
			return True
		else:
			return False

	def is_empty(self):
		return self.stack == []

	def get_top(self):
		return self.stack[::-1][0]

	def get_data(self):
		return self.stack[::-1]

	def print_stack(self):
		for el in self.get_data():
			print(el)


