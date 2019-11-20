# Dequeue Implementation
class Dequeue: 
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

d = Dequeue()
print(d.isEmpty())

d.addRear(4)
d.addRear('dog')
print(d.items)

d.addFront('cat')
d.addFront(True)
print(d.items)

print(d.removeRear())
print(d.removeFront())

print(d.size())

# Palindrome Checker
# - a palindrome is a string that reads the same forward and backward, ex. racecar

def palChecker(astring):
	dq = Dequeue()

	for ch in astring:
		dq.addRear(ch)

	stillEqual = True

	while dq.size() > 1 and stillEqual:
		first = dq.removeFront()
		last = dq.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual

print(palChecker("tester"))
print(palChecker("racecar"))