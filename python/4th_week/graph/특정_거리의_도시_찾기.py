import sys
import heapq

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# n, m, k, x = 4, 3, 2, 1
# graph = [[], [2, 3, 4], [], [], []]

INF = int(1e9)

target_distance = k
start_node = x

dist = [INF] * (n + 1)
dist[start_node] = 0
heap = [(0, start_node)]

while heap:
    distance, target_node = heapq.heappop(heap)
    if distance > dist[target_node]:
        continue

    for node in graph[target_node]:
        new_distance = distance + 1
        if new_distance < dist[node]:
            dist[node] = new_distance
            heapq.heappush(heap, (new_distance, node))

if k not in dist:
    print(-1)

for i, d in enumerate(dist):
    if d == k:
        print(i)
