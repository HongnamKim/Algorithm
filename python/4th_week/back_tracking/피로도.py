"""
피로도 사용해서 던전 탐험
던전 - 최소 필요 피로도 + 소모 피로도
    최소 필요 피로도 -> 던전 들어가기 위해 갖고 있어야 하는 피로도
    소모 피로도 -> 던전 탐험 후 소모되는 피로도
"""

from itertools import permutations


def solution(k, dungeons):
    n = len(dungeons)

    nums = [i for i in range(n)]

    max_count = 0
    for p in permutations(nums, r=n):
        dungeon_count = 0
        kk = k
        for i in p:
            if kk >= dungeons[i][0]:  # 현재 피로도가 필요 피로도보다 낮으면
                kk -= dungeons[i][1]  # 던전 탐험
                dungeon_count += 1

        max_count = max(max_count, dungeon_count)
        if max_count == n:
            return max_count

    return max_count


a = 80
b = [[80, 20], [50, 40], [30, 10]]
print(solution(a, b))
