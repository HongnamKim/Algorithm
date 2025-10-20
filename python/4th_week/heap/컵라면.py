import sys
import heapq

input = sys.stdin.readline

n = int(input())

problems = []

reward = 0
for _ in range(n):
    problem = list(map(int, input().split()))
    problems.append(problem)

# 데드라인 기준 정렬
problems.sort(key=lambda p: p[0])

max_problem_count = problems[-1][0]

# reward 기준 최소힙
heap = []

# print(problems)

for problem in problems:
    heapq.heappush(heap, (problem[1], problem))

    if len(heap) > problem[0]:  # and heap[0][0] <= problem[1]:
        heapq.heappop(heap)

    # print(heap)


# print(problems)
# print(heap)

total_reward = 0
for problem in heap:
    total_reward += problem[1][1]

print(total_reward)
