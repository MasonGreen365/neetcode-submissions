class MinStack:
    #define stack and minStack
    def __init__(self):
        self.stack = []
        self.minStack = []

    #push to stack, check against top of minStack and append smallest val 
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    #pop from both
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    #return stack top
    def top(self) -> int:
        return self.stack[-1]

    #return minStack top
    def getMin(self) -> int:
        return self.minStack[-1]
        
