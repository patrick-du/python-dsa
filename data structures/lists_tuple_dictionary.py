# List Implementation []
list1 = ['math', 'english', 1999, 2000]
list2 = [1, 2, 3, 4, 5]

list1[2]= 1997
del list1[3]

print (list1[0])
print(len(list1))

list3 = list1 + list2 
print (list3)
print (list1*4) 
print (3 in list1)
print ('math' in list1)


# Tuple Implementation ()
tup1 = ('physics', 'chem', 'bio', 1995, 1875)
tup2 = (1,2,3,4,5,6,7)

tup3 = () 
tup4 = (50,)

print (tup1[0], tup2[1:5]);

tup5 = tup1 + tup2  #tuples are immutable => cannot be updated, however they can be concatenated to form new tuples
print (tup5)

del tup2 #removing individual tuple elements is not possible but it is possible to remove an entire tuple


# Dictionary Implementation {}
#   - Keys are immutable data types (strings, #s, tuples)
#   - Values are any type

dict1 = {'Name': 'Zara', 'Age': 8, 'Class': 'First'}
print (dict1['Name'], dict1['Age'])

dict1['Age'] = 10 
dict1['School'] = 'DPS School' 
del dict1['Class'] 
print (dict1)

dict1.clear(); 
print (dict1)

del dict1
