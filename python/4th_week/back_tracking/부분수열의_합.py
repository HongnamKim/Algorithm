import sys

input = sys.stdin.readline

n, s = map(int, input().split())

numbers = list(map(int, input().split()))


def count_subseq(numbers, s):
    n = len(numbers)
    ans = 0

    def dfs(i, total):
        nonlocal ans
        if i == n:
            if total == s:
                ans += 1
            return

        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total)

    dfs(0, 0)

    return ans - 1 if s == 0 else ans


print(count_subseq(numbers, s))


def count_subseq_stack(numbers, s):
    n = len(numbers)
    ans = 0
    stack = [(0, 0, False)]

    while stack:
        i, total, picked = stack.pop()
        if i == n:
            if picked and total == s:
                ans += 1
            continue

        stack.append((i + 1, total + numbers[i], True))
        stack.append((i + 1, total, picked))
