# n x n 의 체스판에 n 개의 퀸을 서로 공격할 수 없게


def solution(n):
    answer = 0
    col = []
    ld = []
    rd = []

    # path = []

    def dfs(count):
        nonlocal answer
        nonlocal ld
        nonlocal rd

        if count == n:  # n개의 퀸 배치
            answer += 1
            # print(path)

            return

        # 맨 위에서부터 퀸을 배치
        for i in range(n):
            if (
                i not in col
                and i not in ld
                and i not in rd  # i != left_diagonal and i != right_diagonal
            ):  # 퀸을 같은 열에 둘 수 없음
                # 왼쪽 대각선 아래, 오른쪽 대각선 아래에 둘 수 없음
                col.append(i)

                for j in range(len(ld)):
                    ld[j] -= 1
                    rd[j] += 1

                ld.append(i - 1)
                rd.append(i + 1)

                # path.append(i)
                dfs(count + 1)
                col.pop()
                ld.pop()
                for j in range(len(ld)):
                    ld[j] += 1
                    rd[j] -= 1

                rd.pop()

    dfs(0)

    return answer


a = 4

print(solution(a))


def comb_iter(arr, r):
    n = len(arr)
    out = []
    # 스택: (start_index, path)
    stack = [(0, [])]

    while stack:
        start, path = stack.pop()

        if len(path) == r:
            out.append(path)
            continue

        max_start = n - (r - len(path))

        for i in range(max_start, start - 1, -1):
            stack.append((i + 1, path + [arr[i]]))

    return out


print(comb_iter([1, 2, 3, 4, 5], 3))


def comb(arr, r):
    n = len(arr)
    out = []
    stack = [(0, [])]

    while stack:
        print(stack)
        start, path = stack.pop()

        if len(path) == r:
            out.append(path)
            continue

        max_start = n - (r - len(path))

        for i in range(max_start, start - 1, -1):
            stack.append((i + 1, path + [arr[i]]))

    return out


print(comb([1, 2, 3, 4, 5], 3))
