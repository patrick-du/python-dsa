import collections #chainmap method comes from collections library

#if there are duplicate keys, only value from the first key is preserved
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

#create a single dictionary
print(res.maps, '\n')

#print keys and values in ChainMap
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

#print all elements from the result
print('Elements:')
for key,val in res.items():
	print('{} = {}'.format(key, val))
print()

#find specific value in the result
print('day1 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))
print()

#map reordereding
dict3 = {'day1': 'Mon', 'day2': 'Tue'}
dict4 = {'day3': 'Wed', 'day4': 'Thu'}

res1 = collections.ChainMap(dict3, dict4)
print(res1.maps,'\n')

res2 = collections.ChainMap(dict4, dict3)
print(res2.maps,'\n')

#updating map
dict3['day4'] = 'Fri'
print(res1.maps, '\n')
