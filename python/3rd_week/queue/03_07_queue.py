class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
먼저 넣은 것이 먼저 나온다 (First In First Out - FIFO)

앞에서 빼고, 뒤에서 넣기 때문에 Queue 객체에서 앞과 뒤의 정보를 갖고 있어야 한다. --> head, tail
"""


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)

        # 초기 상태
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # 큐에 데이터가 있는 경우
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is empty!"

        out_node = self.head
        self.head = out_node.next

        return out_node.data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())
