import sys


input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2

# numbers = list(map(int, input().split()))
numbers = [9, 8, 7, 1]
numbers.sort()

results = []
stack = [([], set())]

while stack:
    path, used = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for i in range(n - 1, -1, -1):
        if numbers[i] not in used:
            stack.append((path + [numbers[i]], used | {numbers[i]}))

print("\n".join(results))
