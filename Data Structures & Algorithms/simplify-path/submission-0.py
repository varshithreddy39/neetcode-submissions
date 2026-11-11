class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        s=path.split("/")

        for n in s:
            if n=="" or n==".":
                continue
            elif n=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return "/"+"/".join(stack)
        