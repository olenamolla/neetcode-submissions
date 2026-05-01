class MinStack:

    def __init__(self):
        self._items = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self._items.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self._items.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self._items[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


        
