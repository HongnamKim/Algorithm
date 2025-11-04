from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    INF = int(10e9)
    answer = INF

    queue = deque([(0, x)])
    visited = [False] * (y + 1)

    while queue:
        step, num = queue.popleft()

        if visited[num]:
            continue

        if step >= answer:
            continue
        if num > y:
            continue
        if num == y:
            answer = min(answer, step)
            continue

        queue.append((step + 1, num + n))
        queue.append((step + 1, num * 2))
        queue.append((step + 1, num * 3))

    return answer if answer != INF else -1


a = 10
b = 40
c = 30

aa = solution(a, b, c)
print()
print(aa)
