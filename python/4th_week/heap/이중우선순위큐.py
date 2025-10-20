import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    alive = {}

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == "I":
            while max_heap and not alive[-1 * max_heap[0]]:
                heapq.heappop(max_heap)
            heapq.heappush(max_heap, num * -1)

            while min_heap and not alive[min_heap[0]]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
            alive[num] = True
        elif num == 1:
            while max_heap and not alive[-1 * max_heap[0]]:
                heapq.heappop(max_heap)

            if max_heap:
                remove = -1 * heapq.heappop(max_heap)
                alive[remove] = False

        elif num == -1:
            while min_heap and not alive[min_heap[0]]:
                heapq.heappop(min_heap)

            if min_heap:
                remove = heapq.heappop(min_heap)
                # while min_heap and not alive[remove]:
                #     remove = heapq.heappop(min_heap)
                alive[remove] = False

        # print("max: ", max_heap)
        # print("min: ", min_heap)
        # print("alive: ", alive)
        # print()
    while max_heap and not alive[-1 * max_heap[0]]:
        heapq.heappop(max_heap)
    while min_heap and not alive[min_heap[0]]:
        heapq.heappop(min_heap)

    # print(max_heap)
    # print(min_heap)

    return [-max_heap[0] if max_heap else 0, min_heap[0] if min_heap else 0]


a = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(a))
