# Converting an Integer to a String in Any Base
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(769,10))

# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string
def reverse(s):
    if len(s) > 1:
        s = reverse(s[1:]) + s[:1]
    return s

print(reverse("hellllo dalgjad flg"))

# Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. 
# A string is a palindrome if it is spelled the same both forward and backward. 
# For example: radar is a palindrome. Palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. 
# For example: madam i’m adam is a palindrome.

def removeWhite(s):
    s = s.replace(' ', '')
    return s

def palindrome(s):
    if len(s) < 2: return True
    if s[0] != s[-1]: return False
    return palindrome(s[1:-1])

print(palindrome(removeWhite("racecasdar")))

#
