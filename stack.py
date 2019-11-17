class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


def revstring(mystring):
	stack1 = Stack()
	for letter in mystring:
		stack1.push(letter)

	revstr = ''
	while not stack1.isEmpty():
		revstr = revstr + stack1.pop()	
	return revstr
	

print(revstring("reversethisstring"))
