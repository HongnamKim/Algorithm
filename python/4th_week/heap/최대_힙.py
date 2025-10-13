import sys

input = sys.stdin.readline

n = int(input())

heap = [None]


def insert(heap, x):
    heap.append(x)

    cur_index = len(heap) - 1

    while cur_index > 1:
        parent_index = cur_index // 2

        if heap[parent_index] < heap[cur_index]:
            heap[parent_index], heap[cur_index] = heap[cur_index], heap[parent_index]
            cur_index = parent_index
        else:
            break
    return


def delete(heap):
    if len(heap) == 1:
        return 0

    # 최대값과 힙의 맨 끝값 자리 교체
    heap[1], heap[-1] = heap[-1], heap[1]

    # 값 빼기
    root = heap.pop()

    # heap 재배치
    heap_len = len(heap)
    cur_index = 1

    while cur_index < heap_len:
        max_index = cur_index
        left_index = max_index * 2
        right_index = left_index + 1

        if left_index < heap_len and heap[left_index] > heap[max_index]:
            max_index = left_index
        if right_index < heap_len and heap[right_index] > heap[max_index]:
            max_index = right_index

        if max_index == cur_index:
            break

        heap[max_index], heap[cur_index] = heap[cur_index], heap[max_index]
        cur_index = max_index

    return root


for _ in range(n):
    x = int(input())
    if x == 0:
        print(delete(heap))
    else:
        insert(heap, x)
