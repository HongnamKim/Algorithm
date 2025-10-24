import sys
import heapq

input = sys.stdin.readline

n = int(input())  # node count
bus = int(input())  # edge count

city = [[] for _ in range(n + 1)]


for _ in range(bus):
    start, end, distance = map(int, input().split())
    city[start].append((end, distance))

start_node, end_node = map(int, input().split())


# n = 5
# bus = 8
# city = [[], [(2, 2), (3, 3), (4, 1), (5, 10)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []]
# start_node, end_node = 1, 5

INF = int(1e9)

dist = [INF] * (n + 1)
heap = [(0, start_node)]

while heap:
    distance, target_node = heapq.heappop(heap)
    if distance > dist[target_node]:
        continue

    for node, weight in city[target_node]:
        new_distance = distance + weight
        if dist[node] > new_distance:
            dist[node] = new_distance
            heapq.heappush(heap, (new_distance, node))

print(dist[end_node])
