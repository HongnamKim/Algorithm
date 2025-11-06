def solution(number, k):
    numbers = [0] * len(number)

    for i in range(len(number)):
        numbers[i] = number[i]

    n = len(numbers)
    answer = number[: k + 1]

    stack = [(0, [], [])]  # start, used, path

    while stack:
        start, used, path = stack.pop()

        if path and answer[0] > path[0]:
            continue

        if len(path) == (n - k):
            result = "".join(path)

            answer = max(answer, result)
            continue

        for i in range(n - 1, start - 1, -1):
            if i in used:
                continue

            stack.append((i, used + [i], path + [numbers[i]]))

    return answer


def solution2(number, k):
    stack = []
    for ch in number:
        # 뒤에서 더 큰 수가 왔고, 지울 기회가 남아 있으면 앞의 작은 숫자 제거
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    # 아직 못 지운 만큼은 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)


a = "4177252841"
b = 4

# aa = solution(a, b)
bb = solution2(a, b)
print()
# print(aa)
print(bb)
