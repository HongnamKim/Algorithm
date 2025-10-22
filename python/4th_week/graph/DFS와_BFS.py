import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m, v = map(int, input().split())


dfs_graph = [[] for _ in range(n + 1)]
bfs_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    heapq.heappush(dfs_graph[start], end)
    heapq.heappush(bfs_graph[start], end)
    heapq.heappush(dfs_graph[end], start)
    heapq.heappush(bfs_graph[end], start)


dfs_visited = []


def dfs(g, start_node, visited):
    dfs_visited.append(start_node)

    while g[start_node]:
        nxt = heapq.heappop(g[start_node])
        if nxt not in dfs_visited:
            dfs(g, nxt, visited)

    return


dfs(dfs_graph, v, dfs_visited)

bfs_visited = []
queue = deque([v])
bfs_visited.append(v)

while queue:
    node = queue.popleft()

    while bfs_graph[node]:
        nxt = heapq.heappop(bfs_graph[node])
        if nxt not in bfs_visited:
            bfs_visited.append(nxt)
            queue.append(nxt)

    # for nxt in bfs_graph[node]:
    #     if nxt not in bfs_visited:
    #         bfs_visited.append(nxt)
    #         queue.append(nxt)


print(" ".join(map(str, dfs_visited)))
print(" ".join(map(str, bfs_visited)))
