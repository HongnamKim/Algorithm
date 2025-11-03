import sys

input = sys.stdin.readline

# n,m = map(int, input().split())
n, m = 4, 2
# numbers = list(map(int, input().split()))
numbers = [9, 7, 9, 1]

numbers = sorted(set(numbers))
n = len(numbers)
results = []
stack = [(0, [], [False] * n)]

while stack:
    start, path, used = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    seen = set()
    for i in range(n - 1, start - 1, -1):
        if used[i]:
            continue
        nu = used[:]
        nu[i] = True
        stack.append((start + 1, path + [numbers[i]], nu))

print("\n".join(results))
