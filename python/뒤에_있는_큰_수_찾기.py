def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        print(stack)
        x = numbers[i]
        while stack and stack[-1] <= x:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(x)

    return answer


a = [9, 1, 5, 3, 6, 2]
aa = solution(a)

print()
print(aa)
