class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {')': '(',']': '[','}': '{'}

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1]==mapping[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
    
        