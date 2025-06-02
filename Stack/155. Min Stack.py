class MinStack:

    def __init__(self):
        self.stack = []
        self.min1Val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min1Val:
            self.min1Val = val

    def pop(self) -> None:
        popVal = self.stack.pop()
        if popVal == self.min1Val:
            # Recalculate min1Val since we popped the min
            self.min1Val = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min1Val


#This is alternative approach 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
