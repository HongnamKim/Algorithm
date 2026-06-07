def finalPrices(prices):
    answer = [*prices]
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                answer[i] = prices[i] - prices[j]
                break

    return answer

def solution(prices):
    answer = [*prices]

    stack = [] # index

    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            index = stack.pop()
            answer[index] = prices[index] - prices[i]

        stack.append(i)

    return answer




p = [8,4,6,2,3]
#print(finalPrices(p))
print(solution(p))