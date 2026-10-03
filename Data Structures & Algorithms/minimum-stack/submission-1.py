class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        cur_min = min(val, self.getMin()) if self._min_stack else val
        self._min_stack.append(cur_min)
        self._stack.append(val)

    def pop(self) -> None:
        self._min_stack.pop()
        self._stack.pop()
        
    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
