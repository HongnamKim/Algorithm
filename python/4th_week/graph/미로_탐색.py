import sys
from collections import deque


input = sys.stdin.readline

h, w = map(int, input().split())

land = [[0] * w for _ in range(h)]

for i in range(h):
    line = input()
    for j in range(w):
        land[i][j] = int(line[j])

# h, w = 4, 6
# land = [
#     [1, 0, 1, 1, 1, 1],  #
#     [1, 0, 1, 0, 1, 0],  #
#     [1, 0, 1, 1, 1, 1],  #
#     [1, 1, 1, 0, 1, 1],
# ]

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[False] * w for _ in range(h)]

dist = [[0] * w for _ in range(h)]

queue = deque([(0, 0)])
visited[0][0] = True
dist[0][0] = 1

while queue:

    x, y = queue.popleft()
    if (x, y) == (h - 1, w - 1):
        print(dist[x][y])
        break

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and land[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1
