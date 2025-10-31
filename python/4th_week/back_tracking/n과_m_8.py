import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2
# numbers = list(map(int, input().split()))
numbers = [9, 8, 7, 1]


numbers.sort()

# for p in combinations_with_replacement(numbers, r=m):
#     print(*p)

results = []
stack = [(0, [])]

while stack:
    start, path = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for i in range(n - 1, start - 1, -1):
        stack.append((i, path + [numbers[i]]))

print("\n".join(results))
