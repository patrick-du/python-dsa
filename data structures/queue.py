# Queue
# - data el are allowed on one end but removed from the other end 
# - First In First Out (FIFO) feature, the data el inserted first is the first to be removed
# - queue is implemented in Python using a list 

class Queue:
	def __init__(self):
		self.queue = list()

	def addtoq(self, dataval):
		if dataval not in self.queue:
			self.queue.insert(0, dataval)
			return True
		return False

	def removefromq(self):
		if len(self.queue) > 0:
			return self.queue.pop()
		return("No elements in queue!")

	def size(self):
		return len(self.queue)
	
Queue1 = Queue()

Queue1.addtoq("Mon")
Queue1.addtoq("Tue")
Queue1.addtoq("Wed")
print(Queue1.size()) #3

Queue1.removefromq()
print(Queue1.size()) #2
