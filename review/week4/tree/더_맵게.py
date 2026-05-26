import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_k = (first + 2 * second)
        heapq.heappush(scoville, new_k)
        answer += 1

    return answer if scoville[0] >= K else -1

s = [1, 2]
k = 7

print(solution(s, k))