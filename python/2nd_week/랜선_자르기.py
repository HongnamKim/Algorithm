'''
k, n = map(int, input().split(' '))
lines = []
for i in range(k):
    lines.append(int(input()))
'''

k = 4
n = 11
lines = [802, 743, 457, 539]

def solution(n, lines):
    low = 1
    high = min(lines)
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        served = sum(x // mid for x in lines)

        if served >= n:
            low = mid + 1
            answer = mid
        else:
            high = mid - 1


    return answer


print(solution(n, lines))