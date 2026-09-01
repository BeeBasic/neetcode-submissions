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

        
        for key,values in s1.items():
            if key not in t1 or s1[key] != t1[key]:
                return False
        return True