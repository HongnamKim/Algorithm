class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # LinkedList 는 맨 앞(head)만 저장
    def __init__(self, value):
        self.head = Node(value)

    def size(self):
        size = 0
        cur = self.head
        while cur is not None:
            size += 1
            cur = cur.next

        return size

    def append(self, value):
        cur = self.head
        while cur.next is not None: # linkedlist 의 맨 뒤로 이동
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        # for i in range(index):
        #     cur = cur.next
        #     if cur is None:
        #         break

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            index_node = self.get_node(index - 1)
            new_node.next = index_node.next
            index_node.next = new_node

        return

    def delete_node(self, index):
        target_node = self.get_node(index)
        if target_node is None:
            return

        if index == 0:
            self.head = target_node.next
        else:
            prev_node = self.get_node(index - 1)
            prev_node.next = target_node.next

        return

    def parse_int(self):
        sum = 0
        cur = self.head
        while cur is not None:
            sum = sum * 10 + cur.data
            cur = cur.next

        return sum


def get_linked_list_sum(linked_list_1: LinkedList, linked_list_2: LinkedList) -> int:
    num1 = linked_list_1.parse_int()
    num2 = linked_list_2.parse_int()

    return num1 + num2





linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(52)

linked_list.print_all()
print()

linked_list1 = LinkedList(6)
linked_list1.append(7)
linked_list1.append(8)

linked_list2 = LinkedList(3)
linked_list2.append(5)
linked_list2.append(4)

#print(get_linked_list_sum(linked_list1, linked_list2))

#linked_list.add_node(2, 3)
#linked_list.delete_node(3)

#linked_list.print_all()
#print(linked_list.get_node(0).data)
