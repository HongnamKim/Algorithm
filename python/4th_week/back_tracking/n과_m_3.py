import sys

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 4, 2

results = []
stack = [[]]

while stack:
    path = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for i in range(n, 0, -1):
        stack.append(path + [i])

print(results)


# numbers = [i for i in range(1, n + 1)]
#
#
# results = []
# stack = [[]]
#
# while stack:
#     path = stack.pop()
#
#     if len(path) == m:
#         results.append(" ".join(map(str, path)))
#         continue
#
#     for i in range(n - 1, -1, -1):
#         stack.append(path + [numbers[i]])
#
#
# print("\n".join(results))
