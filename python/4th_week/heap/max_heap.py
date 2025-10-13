class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[cur_index], self.items[parent_index] = (
                    self.items[parent_index],
                    self.items[cur_index],
                )
                cur_index = parent_index
            else:
                break

        return

    def delete(self):
        # 1. 루트 노드와 맨 뒤 노드의 자리를 변경
        self.items[1], self.items[-1] = (
            self.items[-1],
            self.items[1],
        )

        root = self.items.pop()
        cur_index = 1

        # 자리 재조정
        while cur_index != len(self.items) - 1:
            child_1 = cur_index * 2
            child_2 = cur_index * 2 + 1

            max_index = cur_index

            if (
                child_1 <= len(self.items) - 1
                and self.items[child_1] > self.items[cur_index]
            ):
                # 왼쪽 자식 노드가 큰 경우
                max_index = child_1

            if (
                child_2 <= len(self.items) - 1
                and self.items[child_2] > self.items[cur_index]
            ):
                # 오른쪽 자식 노드가 큰 경우
                max_index = child_2

            if max_index == cur_index:
                # 자식 노드보다 큰 경우
                break

            # 부모 노드, 자식 노드 위치 변경
            self.items[cur_index], self.items[max_index] = (
                self.items[max_index],
                self.items[cur_index],
            )
            cur_index = max_index

            # if self.items[child_1] > self.items[cur_index]:
            #     self.items[cur_index], self.items[child_1] = (
            #         self.items[child_1],
            #         self.items[cur_index],
            #     )
            #     cur_index = child_1
            # elif self.items[child_2] > self.items[cur_index]:
            #     self.items[cur_index], self.items[child_2] = (
            #         self.items[child_2],
            #         self.items[cur_index],
            #     )
            #     cur_index = child_2
            # else:
            #     break

        return root


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
max_heap.insert(8)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
print(max_heap.delete())
print(max_heap.items)
