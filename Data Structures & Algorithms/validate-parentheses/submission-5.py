class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        if(len(s)%2==1):
            return False
        if(s[0]=='}' or s[0]==']' or s[0]==')'): 
            return False
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                last=stack.pop()
                if c == '}':
                    if last != '{':
                        return False
                elif c == ']':
                    if last != '[':
                        return False
                elif c == ')':
                    if last != '(':
                        return False
        if len(stack)==0:
            return True
        else:
            return False
            