class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        delete_note = self.head
        self.head = delete_note.next

        return delete_note

    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.head.data

    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(123)
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())

stack.push(321)
print(stack.peek())