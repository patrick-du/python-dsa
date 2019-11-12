# Sorting
# - arranges data in particular order
# - optimizes data searching if stored in sorted manner
# - 5 implementations: bubble sort, merge sort, insertion sort, shell sort, selection sort

# Selection Sort
# - find minimum value in given list and move it to a sorted list
# - repeat proces for each of remaining elements in unsorted list
# - next element entering sorted list is compred with existing elements and placed at its correct position

def selection_sort(input_list):
	for indx in range(len(input_list)):
		min_indx = indx
		for j in range(indx+1, len(input_list)):
			if input_list[min_indx] > input_list[j]:
				min_indx = j

		input_list[indx], input_list[min_indx] = input_list[min_indx], input_list[indx]
		print(input_list)
l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)