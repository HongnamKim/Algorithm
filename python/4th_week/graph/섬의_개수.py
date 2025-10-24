import sys
from collections import deque

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    land = [[0] * w for _ in range(h)]

    for i in range(h):
        line = input().split()
        for j in range(w):
            land[i][j] = int(line[j])

    visited = [[False] * w for _ in range(h)]

    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    island_count = 0

    for i in range(h):
        for j in range(w):
            if land[i][j] == 0 or visited[i][j]:
                continue

            queue = deque([(i, j)])

            island_count += 1

            while queue:

                x, y = queue.popleft()
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < h
                        and 0 <= ny < w
                        and not visited[nx][ny]
                        and land[nx][ny] == 1
                    ):
                        queue.append((nx, ny))
                        visited[nx][ny] = True

    print(island_count)
