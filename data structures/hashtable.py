# Hash Table
# - DS in which index value of data el is generated from a hash function
# - access data faster as index value behaves as a key for the data value AKA key(hashed)-value pairs 
# - implemented in Python with a dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 8; #update existing entry
dict['School'] = 'DPS School'; #add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name'] #delete single entry
print(dict)

dict.clear() #delete all entries
print(dict)

del dict #delete entire dictionary
