# Tree Trversal
# - process to visit all nodes of a tree and print their values
# - all nodes are connected via edges (links) and start from root (head) node
# - 3 ways to traverse a tree
#	- In-order Traversal
#	- Pre-order Traversal
#	- Post-order Traversal

class Node: 
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	# Insert Node
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

	# Print Tree
	def printTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data),
		if self.right: 
			self.right.PrintTree()

	# In-order Traversal
	# Left -> Root -> Right
	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.left)
			res.append(root.data)
			res = res + self.inorderTraversal(root.right)
		return res

	# Pre-order Traversal
	# Root -> Left -> Right
	def preorderTraversal(self, root):
		res = []
		if root:
			res.append(root.data)
			res = res + self.preorderTraversal(root.left)
			res = res + self.preorderTraversal(root.right)
		return res

	# Post-order Traversal
	# Left -> Right -> Root
	def postorderTraversal(self, root):
		res = []
		if root
			res = self.postorderTraversal(root.left)
			res = res + self.postorderTraversal(root.right)
			res.append(root.data)
		return res


root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))