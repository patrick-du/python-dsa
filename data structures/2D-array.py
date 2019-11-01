from array import *

#2D array initialization
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
