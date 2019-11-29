from array import *


#########################################################################


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


#########################################################################


# 2D array initialization
T = [[11, 12, 5, 3], [15, 6, 10], [10, 8, 12, 5], [12, 15, 7, 2]]

#print row 0
print(T[0])

#print row 1, index 2
print(T[1][2])

#print entire 2D array
for r in T:
	for c in r:
		print (c,end = " ") #end by default is '\n' (a new line), in this case we set it to a space
	print () #print a space after each row

#insert data el at index position 2
T.insert(2, [0, 5, 11, 13, 6])
for r in T:
	for c in r:
		print (c, end = " ")
	print ()

#update entire inner array
T[2] = [11, 19]

#update specific data el of inner array
T[0][3] = 99

for r in T: 
	for c in r:
		print (c, end = " ")
	print ()


#########################################################################


from numpy import *

a = array(['Mon',18,20,22,17], ['Tue',11,18,21,18], ['Wed',15,21,20,19], ['Thu',11,20,22,21], ['Fri',18,17,23,22], ['Sat',12,22,20,18], ['Sun',13,15,19,16])

#present 7x5 matrix with numpy reshape method
m = reshape(a, (7,5)) 
print(m)

#print data for wed
print(m[2])

