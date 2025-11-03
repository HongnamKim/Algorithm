import sys

input = sys.stdin.readline

# n,m = map(int, input().split())
n, m = 4, 2
# numbers = list(map(int, input().split()))
numbers = [9, 7, 9, 1]

numbers.sort()
results = []
stack = [([], [False] * n)]

while stack:
    path, used = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    seen = set()
    for i in range(n - 1, -1, -1):
        if used[i]:
            continue
        num = numbers[i]
        if num in seen:
            continue
        seen.add(num)
        nu = used[:]
        nu[i] = True
        stack.append((path + [num], nu))

print("\n".join(results))
