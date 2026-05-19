def solution(prices):
    answer = [0] * len(prices)
    stack = [] # [[price, index]]

    for i in range(len(prices)):
        # if stack and stack[-1][0] >= prices[i]:
        #     _, index = stack.pop()
        #     answer[index] = i - index
        while stack and stack[-1][0] > prices[i]:
            _, index = stack.pop()
            answer[index] = i - index

        stack.append([prices[i], i])

    while stack:
        _, index = stack.pop()
        answer[index] = len(prices) - index - 1

    return answer


prices = [1,2,3,2,3]
print(solution(prices))