class node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def get_value(self):
		return self.value

	def set_next_node(self, next):
		self.next = next

	def get_next_node(self):
		return self.next

class stack:

	def __init__(self,value):
		self.head = node(value)

	def get_head_node(self):
		return self.head

	def is_empty(self):
		return (self.head == None)

	def push(self, next_value):
		new_node = node(next_value)
		new_node.set_next_node(self.head)
		self.head = new_node

	def pop(self):
		if not(self.is_empty()):
			catch = self.head
			self.head= self.head.get_next_node()
		else:
			print("Stack is Empty")

	def command(self, m):
		if m == '-':
			self.pop()
		else:
			self.push(m)
		self.stringify()

	def stringify(self):
		s = ""
		x = self.get_head_node()
		while (x != None):
			s = s + " " + x.value
			x = x.get_next_node()
		print(s)

test = stack('B')
m = input("Input : ")
while (m != '-9999'):
	test.command(m)
	m = input("Input : ")