def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # print(stack)
        x = prices[i]
        while stack and stack[-1][1] > x:  # 주식 가격 떨어짐
            idx, price = stack.pop()
            answer[idx] = i - idx

        stack.append((i, x))

    print(stack)
    while stack:
        idx, price = stack.pop()
        print(n - idx - 1)
        answer[idx] = n - idx - 1

    return answer


a = [1, 2, 3, 2, 3]
aa = solution(a)

print()
print(aa)
