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

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        index = self.size() - k

        return self.get(index)

    def get_kth_node_from_last_improved(self, k):
        slow = self.head
        fast = self.get(k-1)

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        return slow

    def get(self, index):
        count = 0
        cur = self.head
        while count != index:
            cur = cur.next
            count += 1

        return cur

    def size(self):
        size = 0
        cur = self.head
        while cur is not None:
            size += 1
            cur = cur.next

        return size

# [6] -> [7] -> [8] -> [9]

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.size())

print(linked_list.get_kth_node_from_last(4).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_improved(4).data)