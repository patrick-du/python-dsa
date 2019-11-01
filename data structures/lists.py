list1 = ['math', 'english', 1999, 2000]
list2 = [1, 2, 3, 4, 5]

print ("list1[0]: ", list1[0])
print ("list2[0]: ", list2[0])

list1[2]= 1997 #updating list
print ("New value at index 2: ", list1[2])

del list1[3]
print ("Index 3 was deleted, new list: ", list1)

print(len([1,2,3])) #length

list3 = list1 + list2 #concatenation
print (list3)

print (['Hi!']*4) #repetition

print (3 in [1,2,3]) #membership - returns boolean


