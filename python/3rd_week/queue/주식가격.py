from collections import deque


def solution(prices):
    answer = []

    prices = deque(prices)

    while prices:
        current_price = prices.popleft()  # 가장 왼쪽 가격
        days = 0

        for next_price in prices:
            if next_price >= current_price:
                days += 1
            else:
                days += 1
                break

        answer.append(days)

    return answer


def stack_solution(prices):
    length = len(prices)
    answer = [0] * length

    stack = []

    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            idx, prev_price = stack.pop()
            answer[idx] = i - idx

        stack.append((i, price))
        # print(stack)

    while stack:
        idx, price = stack.pop()
        answer[idx] = length - idx - 1

    return answer


prices = [1, 2, 3, 3, 2, 3]
print("input: ", prices)
print(solution(prices))
print(stack_solution(prices))
