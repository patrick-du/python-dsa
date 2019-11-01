# Linked List 
# - sequence of data elements connected via links OR string of nodes, each node containing both data and a reference to the next node in the list
# - each data el contains connection to another data el in form of pointer
# - implemented using concept of nodes in python, it is not a standard concept

# Node Class Definition
class Node: 
	def __init__(self, dataval=None): # Note that __init__ is a reserved method that is called when an object is created from a class and it initializes the class attributes
		self.dataval = dataval
		self.nextval = None

# Singly LinkedList Definition
class SLinkedList: 
	def __init__(self): # Self parameter represents instance of class, it binds the attributes with the given arguments
		self.headval = None

	def listPrint(self): # Print Linked List
		printval = self.headval
		while printval is not None:
			print (printval.dataval)
			printval = printval.nextval

	def atBeginning(self, newdata): # Node Insertion
		NewNode = Node(newdata)
		NewNode.nextval = self.headval
		self.headval = NewNode

	def atEnd(self, newdata):
		NewNode = Node(newdata)
		if self.headval is None: 
			self.headval = NewNode
			return
		last = self.headval
		while(last.nextval):
			last = last.nextval
		last.nextval = NewNode

	def inBetween(self, middle_node, newdata):
		if middle_node is None:
			print("The mentioned node is absent")
			return

		NewNode = Node(newdata)
		NewNode.nextval = middle_node.nextval
		middle_node.nextval = NewNode

	def removeNode(self, removekey):
		Head = self.headval

		if (Head is not None):
			if (Head.dataval == removekey):
				self.headval = Head.nextval
				Head = None
				return

		while (Head is not None):
			if Head.dataval == removekey:
				break
			prev = Head
			Head = Head.nextval

		if (Head == None):
			return

		prev.nextval = Head.nextval
		Head = None

list1 = SLinkedList()
list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2 #Link first Node to second Node
e2.nextval = e3 #Link second Node to third Node

list1.listPrint()

list1.atBeginning("Sun")
list1.listPrint()

list1.atEnd("Thu")
list1.listPrint()

print("hi")
list1.inBetween(list1.headval.nextval, "Fri")
list1.listPrint()
print("hi")

list1.removeNode("Mon")
list1.removeNode("Thu")
list1.removeNode("Fri")
list1.listPrint()

