

def solution(d, budget):
    low = 0
    high = max(d)
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        served = sum(min(mid, i) for i in d)

        if served <= budget:
            ans = mid
            low = mid + 1
        elif served == budget:
            break
        else:
            high = mid - 1

    return ans

n = int(input())
d = list(map(int, input().split(' ')))
budget = int(input())

print(solution(d, budget))