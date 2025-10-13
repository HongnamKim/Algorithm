import sys

input = sys.stdin.readline

n = int(input())

heap = [None]


def insert(heap: list, x: int):
    heap.append(x)

    # 맨 뒤에 집어 넣은 위치
    cur_index = len(heap) - 1

    while cur_index != 1:
        # 부모랑 비교
        parent_index = cur_index // 2
        if heap[parent_index] > heap[cur_index]:
            heap[cur_index], heap[parent_index] = heap[parent_index], heap[cur_index]
            cur_index = parent_index
        else:
            break


def delete(heap):
    if len(heap) == 1:
        return 0

    # 맨 앞과 맨 뒤 위치 변경
    heap[1], heap[-1] = heap[-1], heap[1]

    # 맨 뒤의 값 제거
    output = heap.pop()

    # 위치 재조정
    cur_index = 1

    while cur_index != len(heap) - 1:
        min_index = cur_index
        left_index = cur_index * 2
        right_index = left_index + 1

        if left_index <= len(heap) - 1 and heap[left_index] < heap[min_index]:
            min_index = left_index

        if right_index <= len(heap) - 1 and heap[right_index] < heap[min_index]:
            min_index = right_index

        if min_index == cur_index:
            break

        heap[cur_index], heap[min_index] = heap[min_index], heap[cur_index]

        cur_index = min_index

    return output


for _ in range(n):
    x = int(input())
    if x > 0:
        insert(heap, x)
    else:
        print(delete(heap))

#    print(heap)
