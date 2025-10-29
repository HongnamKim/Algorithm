import sys

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2

results = []
stack = [(0, [])]

while stack:
    print(stack)
    start, path = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    max_start = n - (m - len(path))
    for i in range(max_start, start, -1):
        stack.append((start + 1, path + [i]))

print("\n".join(results))
