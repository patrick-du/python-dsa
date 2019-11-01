# Dequeue
# - double-ended queue
# - add and remove elements from either end 

import collections

Dequeue = collections.deque(["Mon", "Tue", "Wed"])

Dequeue.append("Thu")
print("Appended at right - ")
print(Dequeue)

Dequeue.appendleft("Sun")
print("Appended at left - ")
print(Dequeue)

Dequeue.pop()
print("Deleting from the right - ")
print(Dequeue)

Dequeue.popleft()
print("Deleting from the left - ")
print(Dequeue)