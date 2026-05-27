import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    deleted = set()

    for operation in operations:
        op, number = operation.split(" ")
        number = int(number)
        if op == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -1 * number)

            if number in deleted:
                deleted.remove(number)

        if op == "D":
            if number == 1:
                while max_heap and -1 * max_heap[0] in deleted:
                    heapq.heappop(max_heap)

                if max_heap:
                    pop = -1 * heapq.heappop(max_heap)
                    deleted.add(pop)

            else:
                while min_heap and min_heap[0] in deleted:
                    heapq.heappop(min_heap)

                if min_heap:
                    pop = heapq.heappop(min_heap)
                    deleted.add(pop)

        print(operation)
        print(min_heap)
        print(max_heap)
        print(deleted)
        print()

        while max_heap and -1 * max_heap[0] in deleted:
            heapq.heappop(max_heap)
        while min_heap and min_heap[0] in deleted:
            heapq.heappop(min_heap)

    return [-1 * heapq.heappop(max_heap), heapq.heappop(min_heap)] if max_heap and min_heap else [0,0]

o = ["I 1", "I 2", "D -1", "D 1"]
print(solution(o))