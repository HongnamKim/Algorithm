class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def size(self):
        size = 1
        cur = self.head
        while cur.next is not None:
            size += 1
            cur = cur.next
        return size

    def get_kth_node_from_last(self, k):
        target_index = self.size() - k
        cur_index = 0
        cur = self.head
        while cur_index != target_index:
            cur_index += 1
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.size())

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
