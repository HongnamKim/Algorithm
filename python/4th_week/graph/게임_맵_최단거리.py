from collections import deque


def get_next_position(position, n, m):
    next_position = []

    if position[0] == 0:
        # 아래 방향만 확인
        if position[1] == 0:
            # 오른쪽만 확인
            next_position.append((position[0], position[1] + 1))
            next_position.append((position[0] + 1, position[1]))
        elif position[1] == m - 1:
            # 왼쪽만 확인
            next_position.append((position[0], position[1] - 1))
            next_position.append((position[0] + 1, position[1]))
        else:
            next_position.append((position[0], position[1] + 1))
            next_position.append((position[0], position[1] - 1))
            next_position.append((position[0] + 1, position[1]))
    elif position[0] == n - 1:
        # 윗 방향만 확인
        if position[1] == 0:
            # 위 or 오른쪽만 확인
            next_position.append((position[0], position[1] + 1))
            next_position.append((position[0] - 1, position[1]))
        elif position[1] == m - 1:
            # 위 or 왼쪽만 확인
            next_position.append((position[0], position[1] - 1))
            next_position.append((position[0] - 1, position[1]))
        else:
            next_position.append((position[0] - 1, position[1]))
            next_position.append((position[0], position[1] + 1))
            next_position.append((position[0], position[1] - 1))
    else:
        # 위 아래 확인
        if position[1] == 0:
            # 오른쪽만 확인
            next_position.append((position[0] + 1, position[1]))  # 아래
            next_position.append((position[0] - 1, position[1]))  # 위
            next_position.append((position[0], position[1] + 1))  # 오른쪽
        elif position[1] == m - 1:
            next_position.append((position[0] + 1, position[1]))
            next_position.append((position[0] - 1, position[1]))
            next_position.append((position[0], position[1] - 1))
        else:
            next_position.append((position[0] + 1, position[1]))
            next_position.append((position[0] - 1, position[1]))
            next_position.append((position[0], position[1] + 1))
            next_position.append((position[0], position[1] - 1))

    return next_position


def solution(maps):
    n, m = len(maps), len(maps[0])

    # 시작점 또는 도착점이 0 일 경우 종료
    if maps[0][0] == 0 or maps[-1][-1] == 0:
        return -1

    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]  # 각 좌표 별 최단거리 저장용

    # 탐색 시작 전 설정
    queue = deque([(0, 0)])
    visited[0][0] = True
    dist[0][0] = 1

    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return dist[x][y]

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            # (nx, ny)가 이동 가능한 위치일 경우
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and not visited[nx][ny]
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1

    return -1


m = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
]

print(solution(m))
