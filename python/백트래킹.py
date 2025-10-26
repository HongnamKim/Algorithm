def backtrack(path):
    if len(path) == 3:
        print(path)
        return
    for i in range(1, 5):
        if i not in path:
            backtrack(path + [i])


# backtrack([])

n = 4
m = 2


def foo(start, path):
    if len(path) == m:
        print(*path)
        return
    for i in range(start, n + 1):
        path.append(i)
        foo(i + 1, path)
        path.pop()


# foo(1, [])


def count_subseq_sum(nums, S):
    n = len(nums)

    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]
    print(suffix)

    ans = 0

    def dfs(i, cur):
        nonlocal ans
        if cur > S:
            return

        if cur + suffix[i] < S:
            return

        if i == n:
            ans += cur == S
            return

        dfs(i + 1, cur + nums[i])
        dfs(i + 1, cur)

    dfs(0, 0)
    return ans


print(count_subseq_sum([1, 2, 3, 4, 5, 6, 7, 8], 9))
