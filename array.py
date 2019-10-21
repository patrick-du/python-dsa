from array import *


array1 = array('i', [1,2,3,4,5]) #i represents signed integer of size 2 bytes

for x in array1:
	print(x)

print(array1[0])
print(array1[1])

array1.insert(1,60) #insert at index 1, el 60
print(array1)

array1.remove(4) #delete 4 in the array
print(array1)

print(array1.index(5))

array1[2] = 160 #update index 2 to el 160
print(array1)