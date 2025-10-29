import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]

result = []
path = []
used = [False] * n


def dfs():
    if len(path) == m:
        result.append(" ".join(map(str, path)))
        return

    for i in range(n):
        if used[i]:
            continue
        path.append(numbers[i])
        used[i] = True
        dfs()
        path.pop()
        used[i] = False


dfs()

print("\n".join(result))
