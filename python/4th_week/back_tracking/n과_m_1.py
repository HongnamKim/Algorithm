import sys

# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# numbers = [i for i in range(1, n + 1)]

# result = []
# path = []
# used = [False] * n
#
#
# def dfs():
#     if len(path) == m:
#         result.append(" ".join(map(str, path)))
#         return
#
#     for i in range(n):
#         if used[i]:
#             continue
#         path.append(numbers[i])
#         used[i] = True
#         dfs()
#         path.pop()
#         used[i] = False
#
#
# dfs()
#
# print("\n".join(result))

# n, m = 4, 2
#
# results = []
#
# stack = [([], [False] * (n + 1))]
#
# while stack:
#     path, used = stack.pop()
#
#     if len(path) == m:
#         results.append(" ".join(map(str, path)))
#         continue
#
#     for x in range(n, 0, -1):
#         if not used[x]:
#             new_used = used[:]
#             new_used[x] = True
#             stack.append((path + [x], new_used))
#
#
# print("\n".join(results))

n, m = 4, 2

results = []

stack = [([], set())]

while stack:
    path, used = stack.pop()

    if len(path) == m:
        results.append(" ".join(map(str, path)))
        continue

    for x in range(n, 0, -1):
        if x not in used:
            stack.append((path + [x], used | {x}))

print(results)
