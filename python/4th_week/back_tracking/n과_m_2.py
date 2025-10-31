import sys

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2

# numbers = [i for i in range(1, n + 1)]
#
# results = []
# stack = [(0, [])]  # index, path
#
# while stack:
#     start, path = stack.pop()
#
#     if len(path) == m:
#         results.append(" ".join(map(str, path)))
#         continue
#
#     max_start = n - (m - len(path))
#     for i in range(max_start, start - 1, -1):
#         stack.append((i + 1, path + [numbers[i]]))
#
# print("\n".join(results))


results = []
stack = [(0, [])]

while stack:
    print(stack)
    start, path = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for i in range(n, start, -1):
        stack.append((i, path + [i]))

print("\n".join(results))
