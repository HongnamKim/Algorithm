import sys

input = sys.stdin.readline

n = int(input())

heap = [None]


# 절댓값 최소 힙
def insert(heap, x):
    heap.append((abs(x), x))

    cur_index = len(heap) - 1

    while cur_index > 1:
        parent_index = cur_index // 2

        if heap[parent_index][0] > heap[cur_index][0]:
            heap[parent_index], heap[cur_index] = heap[cur_index], heap[parent_index]
            cur_index = parent_index
        elif (
            heap[parent_index][0] == heap[cur_index][0]
            and heap[parent_index][1] > heap[cur_index][1]
        ):
            heap[parent_index], heap[cur_index] = heap[cur_index], heap[parent_index]
            cur_index = parent_index
        else:
            break


def delete(heap):
    if len(heap) == 1:
        return 0

    heap[1], heap[-1] = heap[-1], heap[1]

    root = heap.pop()

    cur_index = 1
    heap_len = len(heap)

    while cur_index < heap_len:
        min_index = cur_index
        left_index = min_index * 2
        right_index = left_index + 1

        if left_index < heap_len and heap[left_index][0] < heap[min_index][0]:
            min_index = left_index
        if (
            left_index < heap_len
            and heap[left_index][0] == heap[min_index][0]
            and heap[left_index][1] < heap[min_index][1]
        ):
            min_index = left_index

        if right_index < heap_len and heap[right_index][0] < heap[min_index][0]:
            min_index = right_index
        if (
            right_index < heap_len
            and heap[right_index][0] == heap[min_index][0]
            and heap[right_index][1] < heap[min_index][1]
        ):
            min_index = right_index

        if min_index == cur_index:
            break

        heap[cur_index], heap[min_index] = heap[min_index], heap[cur_index]
        cur_index = min_index

    return root[1]


answer = []

for i in range(n):
    x = int(input())
    if x != 0:
        insert(heap, x)
    else:
        answer.append(str(delete(heap)))

print("\n".join(answer))
