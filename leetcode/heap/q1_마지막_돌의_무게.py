import heapq

def lastStoneWeight(stones):
    stones = list(map(lambda x: -1 * x, stones))

    heapq.heapify(stones)

    while len(stones) > 1:
        stone1 = -1 * heapq.heappop(stones)
        stone2 = -1 * heapq.heappop(stones)

        if stone1 - stone2 > 0:
            heapq.heappush(stones, stone2 - stone1)

    return -stones[0] if stones else 0


s = [2,7,4,1,8,1]
print(lastStoneWeight(s))