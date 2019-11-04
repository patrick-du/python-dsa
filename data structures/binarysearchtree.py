#Binary Search Tree (BST)
# - left sub-tree of a node has a key <= parent node's key
# - right sub-tree of a node has a key > parent node's key
# - BST divides all of its sub-trees into two segments 
# 	 - left sub-tree <= node <= right sub-tree

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
		 
	def findval(self, lkpval):
		if lkpval < self.data:
			if self.left is None:
				return str(lkpval) + " is not found"
			return self.left.findval(lkpval)
		elif lkpval > self.data:
			if self.right is None:
				return str(lkpval) + " is not found"
			return self.right.findval(lkpval)
		else: 
			return(str(self.data) + " is found")

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data),
		if self.right:
			self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(52)
root.insert(7)
root.insert(19)
root.insert(14)
root.insert(3)

root.PrintTree()
print(root.findval(19))
print(root.findval(8))