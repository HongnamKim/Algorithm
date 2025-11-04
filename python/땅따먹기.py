import heapq


def solution(land):
    n = len(land)
    dp = land[0][:]

    for i in range(1, n):
        a0, a1, a2, a3 = dp
        dp = [
            land[i][0] + max(a1, a2, a3),
            land[i][1] + max(a0, a2, a3),
            land[i][2] + max(a0, a1, a3),
            land[i][3] + max(a0, a1, a2),
        ]
        print(dp)

    return max(dp)


def solution2(land):
    n = len(land)


a = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
aa = solution(a)
print("--------result--------")
print(aa)
