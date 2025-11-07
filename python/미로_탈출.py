from collections import deque

DIRS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def find_points(maps):
    points = {"S": [-1, -1], "L": [-1, -1], "E": [-1, -1]}

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                points["S"][0], points["S"][1] = i, j
            elif maps[i][j] == "L":
                points["L"][0], points["L"][1] = i, j
            elif maps[i][j] == "E":
                points["E"][0], points["E"][1] = i, j

    return points


def move(maps, s, l):
    n = len(maps[0])
    m = len(maps)

    visited = [[False] * n for _ in range(m)]
    visited[s[0]][s[1]] = True
    queue = deque([(0, s[0], s[1])])  # (거리, i, j)

    while queue:
        distance, y, x = queue.popleft()

        if (y, x) == (l[0], l[1]):
            return distance

        for dy, dx in DIRS:
            ny, nx = y + dy, x + dx

            if (
                0 <= ny < m
                and 0 <= nx < n
                and not visited[ny][nx]
                and maps[ny][nx] != "X"
            ):
                queue.append((distance + 1, ny, nx))
                visited[ny][nx] = True

    return -1


def solution(maps):

    points = find_points(maps)
    S = points["S"]
    if S[0] == -1 or S[1] == -1:
        return -1
    L = points["L"]
    if L[0] == -1 or L[1] == -1:
        return -1
    E = points["E"]
    if E[0] == -1 or E[1] == -1:
        return -1

    s_to_l = move(maps, S, L)
    if s_to_l == -1:
        return -1

    l_to_e = move(maps, L, E)
    if l_to_e == -1:
        return -1

    return s_to_l + l_to_e


a = ["SOOOOL", "XXXXXO", "OOOOOO", "OXXXXX", "OOOOOE"]
aa = solution(a)

print()
print(aa)
