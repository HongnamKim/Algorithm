from collections import defaultdict


def solution(clothes):
    answer = 1

    category_count = defaultdict(int)

    for _, cat in clothes:
        category_count[cat] += 1

    for k in category_count:
        answer *= ((category_count[k]) + 1)

    return answer - 1

c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(c))
