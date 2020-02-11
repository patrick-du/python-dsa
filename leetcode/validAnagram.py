class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        l1 = list(s.encode())
        l2 = list(t.encode())
        l1.sort()
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False
        
    def solution1(self, s, t):
        d = {}
        if len(s) != len(t):
            return False
        
        for c in s:  
            if d.get(c) == None:
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if d.get(c) != None:
                d[c] -= 1
                if d[c] == 0:
                    d.pop(c)
        if d:
            return False
        else:
            return True