import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

map = [[0] * n for _ in range(n)]

for i in range(n):
    m = input()
    for j in range(n):
        map[i][j] = int(m[j])

# map = [
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0],
# ]
#
# n = len(map)

visited = [[False] * n for _ in range(n)]

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

total_groups = 0
group_counts = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 0 or visited[i][j]:
            continue

        total_groups += 1
        queue = deque([(i, j)])
        visited[i][j] = True

        current_group_count = 0
        while queue:
            x, y = queue.popleft()
            current_group_count += 1

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and map[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    queue.append((nx, ny))
                    visited[nx][ny] = True

        group_counts.append(current_group_count)

print(total_groups)
group_counts.sort()
print("\n".join(str(s) for s in group_counts))
print("\n".join(list(map(str, group_counts))))
