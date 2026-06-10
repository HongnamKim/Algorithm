class MyQueue:

    def __init__(self):
        self.forward = []
        self.reverse = []

    def push(self, x: int) -> None:
        self.forward.append(x)


    def pop(self) -> int:
        if not self.reverse:
            while self.forward:
                self.reverse.append(self.forward.pop())

        return self.reverse.pop()


    def peek(self) -> int:
        if not self.reverse:
            while self.forward:
                self.reverse.append(self.forward.pop())

        return self.reverse[-1]

    def empty(self) -> bool:
        return len(self.forward) == 0 and len(self.reverse) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())