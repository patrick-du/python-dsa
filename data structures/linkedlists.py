# Linked List Implementation
# Node Implementation
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

temp = Node(93)
print(temp.getData())

# Unordered Linked List Implementation
class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item);
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else: 
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		# Searching Part
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		# Removal Part
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

mylist1 = UnorderedList()
mylist1.add(31)
mylist1.add(77)
mylist1.add(17)
mylist1.add(93)
mylist1.add(26)
mylist1.add(54)
print(mylist1.isEmpty())
print(mylist1.size())
print(mylist1.search(31))
mylist1.remove(93)
print(mylist1.size())
print(mylist1.search(93))

# Ordered Linked List Implementation
class OrderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current!= None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else: 
					current = current.getNext()
		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(current)
			self.head = temp
		else: 
			temp.setNext(current)
			previous.setNext(temp)

mylist2 = OrderedList()
mylist2.add(31)
mylist2.add(77)
mylist2.add(17)
mylist2.add(93)
mylist2.add(26)
mylist2.add(54)

print(mylist2.size())
print(mylist2.search(93))
print(mylist2.search(100))