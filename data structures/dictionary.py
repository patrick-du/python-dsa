# keys are immutable data types (strings, #s, tuples)
# values are any type

#dictionary initialization
dict1 = {'Name': 'Zara', 'Age': 8, 'Class': 'First'}

#access values in dictionary
print (dict1['Name'])
print (dict1['Age'])

#update existing entry
dict1['Age'] = 10 
print (dict1)

#add new entry
dict1['School'] = 'DPS School' 
print (dict1)

#remove entry with key name
del dict1['Age'] 
print (dict1)

#remove all entries in dictionary
dict1.clear(); 
print (dict1)

#delete entire dictionary 
del dict1
print(dict1)
