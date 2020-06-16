# 1.2 Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other

def checkPermutation(s1, s2): 
    if len(s1) != len(s2):
        return False

    L1 = list(map(lambda x: x, s1))
    L2 = list(map(lambda x: x, s2))
    L1.sort()
    L2.sort()
    return L1 == L2
    

print(checkPermutation('abcd', 'bacd'),) #Expect True
print(checkPermutation('3563476', '7334566')) #Expect True
print(checkPermutation('wef34f', 'wffe34')) #Expect True

print(checkPermutation('abcd', 'd2cba'),) #Expect False
print(checkPermutation ('2354', '1234')) #Expect False
print(checkPermutation('dcw4f', 'dcw5f')) #Expect False