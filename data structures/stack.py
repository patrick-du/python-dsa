# Stack Implementation
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

# Reverse a string
def revstring(mystring):
	stack1 = Stack()
	for letter in mystring:
		stack1.push(letter)

	revstr = ''
	while not stack1.isEmpty():
		revstr = revstr + stack1.pop()	
	return revstr
	
print(revstring("string"))

# Simple Balanced Parentheses
def balanceChecker(stringparam):
	s = Stack()
	balanced = True
	index = 0
	while index < len(stringparam) and balanced:
		currentIteration = stringparam[index]
		if currentIteration == "(":
			s.push(currentIteration)
		else:
			if s.isEmpty():
				balanced = False
			else: 
				s.pop()

		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print(balanceChecker('(()())(()()()()()(((()))))'))

# Balanced Parentheses Checker
def balanceParentheses(stringparam):
	s = Stack()
	balanced = True
	index = 0
	while index < len(stringparam) and balanced:
		symbol = stringparam[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else: 
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1
	if balanced and s.isEmpty():
		return True
	else: 
		return False

def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

print(balanceParentheses('{({([][])}())}'))
print(balanceParentheses('[{()]'))