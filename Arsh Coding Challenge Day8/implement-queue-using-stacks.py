from collections import deque

class MyQueue:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.popleft()

    def isEmpty(self) -> bool:
        return len(self.que) == 0

    def peek(self) -> int:
        if not self.isEmpty():
            return self.que[0]
        return None

    def empty(self) -> bool:
        return self.isEmpty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
