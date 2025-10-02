class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None # 가장 마지막 노드를 가리킴

    # 추가
    def push(self, value):
        last_node = self.head
        new_node = Node(value)

        self.head = new_node
        new_node.next = last_node

        return

    # 제거
    def pop(self):
        delete_node = self.head
        self.head = delete_node.next

        return

    # 맨 앞 노드
    def peek(self):
        return self.head

    def is_empty(self):
        return False if self.head is not None else True

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop().data)

