# Sorting
# - arranges data in particular order
# - optimizes data searching if stored in sorted manner
# - 5 implementations: bubble sort, merge sort, insertion sort, shell sort, selection sort

# Insertion Sort
# - finding right place for given element in sorted list
# - compare first two el and sort them by comparing
# - pick third el and find proper position among the prev two sorted el
# - gradually add more el to already sorted list and putting them in proper position

def insertion_sort(inputList):
	for i in range(1, len(inputList)):
		j = i-1
		nxt_element = inputList[i]	

		while (inputList[j] > nxt_element) and (j >= 0):
			inputList[j+1] = inputList[j]
			j=j-1

		inputList[j+1] = nxt_element

list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)