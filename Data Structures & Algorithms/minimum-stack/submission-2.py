class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float('inf')]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.getMin():
            self.minimum.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
