class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for ch in tokens:
            if ch not in ['+', '-', '*', '/']:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()

                if ch=="+":
                    result = a + b
                elif ch=="-":
                    result=a-b
                elif ch=="*":
                    result=a*b
                elif ch == '/':
                    result = int(a / b)
                stack.append(result)
        return stack[-1]
        
        