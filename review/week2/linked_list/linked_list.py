class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node(5)
second_node = Node(12)
first_node.next = second_node  # 수동으로 node 를 만들고, 연결하는 작업을 거쳐야 함


class LinkedList:
    def __init__(self, value):
        # head 에 첫 시작 Node 지정, LinkedList 객체는 Head 에 대한 정보를 갖는다.
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:  # cur 의 다음 node 가 없을 때까지 (마지막 node까지)
            cur = cur.next
        cur.next = Node(value)  # 마지막 node 에 새로운 값을 가진 node 를 연결

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur_index = 0
        cur = self.head
        while cur_index != index:
            cur_index += 1
            cur = cur.next

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index - 1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            new_head = self.head.next
            self.head = new_head
            return
        prev_node = self.get_node(index - 1)
        prev_node.next = prev_node.next.next


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = 0
    cur1 = linked_list_1.head
    while cur1 is not None:
        sum1 = sum1 * 10 + cur1.data
        cur1 = cur1.next

    sum2 = 0
    cur2 = linked_list_2.head
    while cur2 is not None:
        sum2 = sum2 * 10 + cur2.data
        cur2 = cur2.next

    return sum1 + sum2


linked_list = LinkedList(5)
# print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)
linked_list.print_all()

print(linked_list.get_node(2).data)

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print("\nlinked_list_sum")
print(get_linked_list_sum(linked_list_1, linked_list_2))
