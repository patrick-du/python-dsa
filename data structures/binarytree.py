#Binary Tree
# - non-linear data structure represented by nodes connected by edges
# - properties
#	 - one node is marked as root node
#	 - every node other than the root is associted with one parent node
#	 - each node can have an arbiatry number of child node

class Node:
	def __init__(self, data):
		self.left = None 
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data = data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data),
		if self.right:
			self.right.PrintTree()

root = Node(10)
root.insert(6)
root.insert(52)
root.insert(7)
root.insert(19)
root.insert(14)
root.insert(3)

root.PrintTree()