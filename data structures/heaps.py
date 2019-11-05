#Heaps
# - special tree structure
# 	 - if each parent node is <= child node, it is a min heap
#	 - if each parent node is >= child node, it is a max heap
# - useful in implementing priority ueues where queue item with higher weightage is given more priority in procesing 

#Methods
# - heapify: converts regular list to heap and smallest el gets pushed to index 0, rest of el are not necessarily sorted
# - heappush: adds element to heap without altering current heap
# - heappop: returns smallest el from heap
# - heapreplace: replace smallest el with new value 

import heapq

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

heapq.heappush(H, 8)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H,6)
print(H)