class MyQueue:

    def __init__(self):
        self.value=[]
        

    def push(self, x: int) -> None:
        return self.value.append(x)
        

    def pop(self) -> int:
        if not self.value:
            return 0
        return self.value.pop(0)
        

    def peek(self) -> int:
        if not self.value:
            return 0
        return self.value[0]
        

    def empty(self) -> bool:
        return len(self.value)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()