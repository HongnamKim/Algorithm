n = int(input())
arr = list(map(int, input().split()))


def solution(n, arr):
    stack = []
    answer = ["-1"] * len(arr)

    for i, num in enumerate(arr):
        while stack and stack[-1][1] < num:
            idx, prev_num = stack.pop()
            answer[idx] = str(num)

        stack.append([i, num])

    return " ".join(answer)


# n = 4
# arr = [9, 5, 4, 8]

print(solution(n, arr))
