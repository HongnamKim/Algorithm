from collections import deque

def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])

    # 시작점 또는 도착점이 없는 경우
    if maps[0][0] == 0 or maps[-1][-1] == 0:
        return -1

    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)] # 각 좌표 별 최단거리

    queue = deque([(0,0)])
    visited[0][0] = True
    dist[0][0] = 1

    DIRS = [(1,0), (0,1), (-1, 0), (0,-1)]

    while queue:
        x, y = queue.popleft()
        # 도착점에 도달한 경우
        if (x, y) == (n - 1, m-1):
            return dist[x][y]

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]==1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny]=True
                dist[nx][ny] = dist[x][y] + 1

    return -1

map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(map))