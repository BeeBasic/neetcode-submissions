class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s1 = {}
        for c in s:
            if c in s1:
                s1[c]+= 1
            else:
                s1[c] = 1

        t1={}

        for c in t:
            if c in t1:
                t1[c]+= 1
            else:
                t1[c] = 1

        
        if t1 != s1: return False
        return True