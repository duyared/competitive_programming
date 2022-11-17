class MinStack:

    def __init__(self):
        self.stack = []
        self.top_index = -1
        

    def push(self, val: int) -> None:
        self.top_index += 1
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.top_index -= 1
        

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return min(self.stack)
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
