# 11403
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

g = [[0] * n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        g[i][j] = line[j]

# n = 7
# g = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 0],
# ]

ans = [[0] * n for _ in range(n)]

for i in range(n):
    visited = [False] * n
    queue = deque([i])

    while queue:
        x = queue.popleft()
        for y in range(n):
            if g[x][y] == 1 and not visited[y]:
                queue.append(y)
                visited[y] = True

    for j in range(n):
        if visited[j]:
            ans[i][j] = 1

for i in range(n):
    print(" ".join(map(str, ans[i])))
