def solution(arr):
    stack = [arr[0]]
    for i in range(len(arr)):
        num = arr[i]
        if stack:
            if stack[-1] == num:
                continue
            else:
                stack.append(num)

    return stack


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))
