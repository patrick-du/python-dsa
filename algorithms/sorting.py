# Sorting
# - arranges data in particular order
# - optimizes data searching if stored in sorted manner
# - 5 implementations: bubble sort, merge sort, insertion sort, shell sort, selection sort

# Bubble Sort
# - comparison-based algorithm where pair of adjacent elements are compared and swapped if not in order

def bubblesort(list):
	for iter_num in range(len(list)-1,0,-1): #range(start, stop, step) - in this case, counting down
		for indx in range(iter_num):

			print ("Iteration number is {}".format(iter_num))
			print ("Index is {}".format(indx))

			if list[indx]>list[indx+1]:
				temp = list[indx]
				list[indx] = list[indx+1]
				list[indx+1] = temp
				print(list)

list = [19,2,31,45,6,11,121,27]
bubblesort(list)


