from collections import defaultdict


def solution(weights):
    seen = defaultdict(int)
    ans = 0

    for w in weights:
        # 1:1
        ans += seen[w]

        # 2:1 (짝이 더 가벼웠던 경우)
        if w % 2 == 0:
            ans += seen[w // 2]
        # 3:2
        if (3 * w) % 2 == 0:
            ans += seen[(3 * w) // 2]
        # 4:3
        if (4 * w) % 3 == 0:
            ans += seen[(4 * w) // 3]

        # 1:2 (짝이 더 무거웠던 경우)
        ans += seen[2 * w]
        # 2:3
        if (2 * w) % 3 == 0:
            ans += seen[(2 * w) // 3]
        # 3:4
        if (3 * w) % 4 == 0:
            ans += seen[(3 * w) // 4]

        # 현재 무게 등록 (중복 카운트 방지 위해 마지막에)
        seen[w] += 1

    return ans


a = [100, 180, 360, 100, 270]
aa = solution(a)

print()
print(aa)
