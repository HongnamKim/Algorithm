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


def sample(numbers):
    numbers.sort()
    n = len(numbers)
    used = [False] * n
    results = []
    path = []

    def dfs():
        if len(path) == n:
            results.append(int("".join(map(str, path))))

            return

        for i in range(n):
            if used[i]:
                # 이미 사용한 숫자 제외
                continue

            used[i] = True
            path.append(numbers[i])
            dfs()
            used[i] = False
            path.pop()

    dfs()
    print(results)


# sample([1, 1, 3])


def combination(numbers, r):
    results = []
    n = len(numbers)
    numbers.sort()
    used = [False] * n
    path = []

    # 순열을 만들 때는 start 가 필요
    # 1을 포함한 조합을 만들고 다음 단계에서 1이 또 포함되면 안됨
    def dfs(start):
        # 조건 달정
        if len(path) == r:
            results.append(tuple(path))
            return

        for i in range(start, n):
            if used[i]:
                continue
            if (
                i > 0 and numbers[i] == numbers[i - 1] and not used[i - 1]
            ):  # 조합의 두번째 이상 숫자를 집어넣으려는데, 이전에 같은 숫자가 존재하지만, 사용하지 않음
                # 이전에 같은 조합을 만들어냄 ex [1,1,2,3] --> (numbers[0], numbers[2], numbers[3]), (numbers[1], numbers[2], numbers[3])
                continue
            used[i] = True
            path.append(numbers[i])
            dfs(i + 1)
            path.pop()
            used[i] = False

    dfs(0)

    return results


print(combination([2, 2, 3, 4, 5, 6], 3))


def generate_bracket(n):
    # n: 열린괄호 개수
    results = []
    path = []

    def dfs(open_cnt, close_cnt):
        if open_cnt == n and close_cnt == n:
            results.append("".join(path))
            return

        if open_cnt < n:
            path.append("(")
            dfs(open_cnt + 1, close_cnt)
            path.pop()
        if close_cnt < open_cnt:
            path.append(")")
            dfs(open_cnt, close_cnt + 1)
            path.pop()

    dfs(0, 0)

    return results


print(generate_bracket(3))


def combination_sum(numbers, target):
    n = len(numbers)
    numbers.sort()
    results = []
    path = []

    def dfs(start, total):
        print(path)
        if total == target:
            results.append(path.copy())
            return

        for i in range(start, n):
            if total + numbers[i] <= target:
                path.append(numbers[i])
                dfs(i, total + numbers[i])
                path.pop()

    dfs(0, 0)
    return results


print(combination_sum([2, 3, 6, 7], 7))  # [[2,2,3], [7]
