# Stack
# - stores data el on top of each others and only allow operations at one end
# - Last in First out (LIFO) feature, the data el inserted last in sequence will be the first to come out
# - Adding = PUSH 
# - Removing = POP
# - stack is implemented in Python using an array 


class Stack:
	def __init__(self):
		self.stack = []

	def add(self, dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
			return True
		else: 
			return False

	def remove(self):
		if len(self.stack) <= 0:
			return ("No element in the Stack")
		else:
			return self.stack.pop()
	
	def peek(self):
		return self.stack[-1] #peek top of stack

Stack1 = Stack()
Stack1.add("Mon")
Stack1.add("Tue")
print(Stack1.peek()) #Tue

Stack1.add("Wed")
Stack1.add("Thu")
print(Stack1.peek()) #Thu

Stack1.remove()
print(Stack1.peek()) #Wed
