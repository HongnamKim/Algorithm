import heapq


def insert(heap, s):
    heap.append(s)

    cur_index = len(heap) - 1

    while cur_index != 1:
        parent_index = cur_index // 2
        if heap[parent_index] > heap[cur_index]:
            heap[parent_index], heap[cur_index] = heap[cur_index], heap[parent_index]

            cur_index = parent_index
        else:
            break

    return s


def delete(heap):
    heap[1], heap[-1] = heap[-1], heap[1]

    cur_index = 1

    root = heap.pop()

    heap_len = len(heap)
    while cur_index < heap_len:
        min_index = cur_index

        left_index = min_index * 2
        right_index = left_index + 1
        if left_index < heap_len and heap[min_index] > heap[left_index]:
            min_index = left_index
        if right_index < heap_len and heap[min_index] > heap[right_index]:
            min_index = right_index

        if cur_index == min_index:
            break

        heap[min_index], heap[cur_index] = heap[cur_index], heap[min_index]
        cur_index = min_index

    return root


def solution2(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
        answer += 1

    return answer if scoville[0] >= K else -1


def solution(scoville, K):
    heap = [*scoville]
    heapq.heapify(heap)

    heap = [None] + heap

    # print(heap)

    # for k in scoville:
    #     insert(heap, k)

    answer = 0
    while len(heap) > 2:
        if heap[1] >= K:
            return answer

        a = delete(heap)
        b = delete(heap)
        insert(heap, a + 2 * b)
        answer += 1

    return answer if heap[1] >= K else -1


a = [12, 2, 3, 9, 10, 1]
K = 7

print(solution(a, K))
print(solution2(a, K))
