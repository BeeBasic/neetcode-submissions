class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        br = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        if(len(s)%2==1):
            return False
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                
                last=stack.pop()
                if last != br[c]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
            