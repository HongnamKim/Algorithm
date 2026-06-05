def finalPrices(prices):
    answer = [*prices]
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                answer[i] = prices[i] - prices[j]
                break

    return answer

p = [8,4,6,2,3]
print(finalPrices(p))