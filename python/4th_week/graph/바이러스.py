import sys

input = sys.stdin.readline

computer_count = int(input())  # 100 이하
edge_count = int(input())

graph = [[] for _ in range(computer_count + 1)]

for _ in range(edge_count):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (computer_count + 1)

stack = [1]


count = 0
while stack:
    node = stack.pop()
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            stack.append(nxt)
            visited[nxt] = True
            count += 1

print(count)
