from collections import deque
import heapq


def solution(jobs):
    request_heap = [(x[1], x[0], i, x) for i, x in enumerate(jobs)]
    heapq.heapify(request_heap)

    print(request_heap)

    time = 0
    work_queue = deque()
    while jobs:
        for j in jobs:
            if j[0] <= time:
                work_queue.append(j)

    print(request_heap)

    answer = 0
    return answer


j = [[0, 3], [1, 9], [3, 5]]
print(solution(j))
