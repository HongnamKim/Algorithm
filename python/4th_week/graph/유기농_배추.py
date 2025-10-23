import sys

input = sys.stdin.readline

t = int(input())


def solution():
    m, n, k = map(int, input().split())

    land = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())

        land[y][x] = 1

    # m, n, k = 10, 8, 17
    # land = [
    #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    visited = [[False] * m for _ in range(n)]

    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    land_count = 0

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visited[i][j]:
                continue

            land_count += 1
            stack = [(i, j)]
            visited[i][j] = True

            land_area = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy

                    # if i == 4 and j == 7:
                    #     print(
                    #         "nx, ny: ",
                    #         nx,
                    #         ny,
                    #         0 <= nx < n and 0 <= ny < m,
                    #         # and land[nx][ny] == 1,
                    #         # and not visited[nx][ny],
                    #     )

                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and land[nx][ny] == 1
                        and not visited[nx][ny]
                    ):
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        land_area += 1

            # print(land_area)

    return land_count


for _ in range(t):
    print(solution())
