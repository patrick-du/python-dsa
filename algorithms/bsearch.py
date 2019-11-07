# Binary Search 
# - sorted list of elements and start looking for an element at the middle of the list
# - if search value matches middle value, search is complete
# - otherwise, eliminate hlf the list of elements by choosing whether to proces with right or left half depending on value searched
# - only works because lit is sorted and much quicker than linear search

#Iterative Approach
def bsearch(list, val):
	list_size = len(list) - 1

	idx0 = 0
	idxn = list_size

	while idx0 <= idxn:
		midval = (idx0 + idxn) // 2

		if list[midval] == val:
			return midval

		if val > list[midval]:
			idx0 = midval + 1
		else:
			idxn = midval - 1

	if idx0 > idxn:
		return None

list = [2,7,19,34,53,72]

#print(bsearch(list, 5))
#print(bsearch(list, 53))

# Recursion
# - allows a function to call itself
# - set criteria to decide when recursive call ends

def rbsearch(list, idx0, idxn, val):
	if (idxn < idx0):
		return None
	else:
		midval = idx0 + ((idxn - idx0) // 2)

		if list[midval] > val:
			print(idx0, idxn)
			return rbsearch(list, idx0, midval-1, val)
		elif list[midval] < val:
			print(idx0, idxn)
			return rbsearch(list, midval + 1, idxn, val)
		else: 
			print(idx0, idxn)
			return midval

list = [8,11,24,56,88,131,161]

print(rbsearch(list, 0, 6, 24))
print(rbsearch(list, 0, 6, 51))