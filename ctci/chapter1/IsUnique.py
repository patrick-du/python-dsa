# 1.1 Is Unique
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure?

def isUnique(s): 
    d = {}
    for letter in s:
        if d.get(letter) == 1:
            return False
        else:
            d[letter] = 1
    return True

print(isUnique("test")) #Expect False
print(isUnique("tesadbjom")) #Expect True
print(isUnique("json")) #Expect True
print(isUnique("cracking")) #Expect False



