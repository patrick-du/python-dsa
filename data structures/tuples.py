tup1 = ('physics', 'chem', 'bio', 1995, 1875)
tup2 = (1,2,3,4,5,6,7)

tup3 = () #empty tuple initialization
tup4 = (50,) #tuple containing a single value

print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);

#tuples are immutable => cannot be updated, however they can be concatenated to form new tuples
tup5 = tup1 + tup2 
print (tup5)

#removing individual tuple elements is not possible but it is possible to remove an entire tuple

del tup2  
print (tup2) #produces error