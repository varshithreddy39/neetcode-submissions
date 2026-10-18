class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
         if not self.stack:
            self.stack.append((val, val))
         else:
            curr_min=self.stack[-1][1]
            curr_min=min(curr_min,val)
            self.stack.append((val,curr_min))

    def pop(self) -> None:
         return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
