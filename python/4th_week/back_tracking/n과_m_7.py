import sys
from itertools import permutations, product, repeat

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2
# numbers = list(map(int, input().split()))
numbers = [9, 8, 7, 1]

numbers.sort()
results = []
stack = [[]]

while stack:
    path = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for i in range(n - 1, -1, -1):
        stack.append(path + [numbers[i]])

print("\n".join(results))
print()
for p in product(numbers, repeat=m):
    print(*p)
