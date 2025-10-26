import sys
from itertools import combinations

input = sys.stdin.readline

heights = []

for _ in range(9):
    heights.append(int(input()))


heights.sort()

# 합이 100이 되는 조합 찾기
for c in combinations(heights, r=7):
    if sum(c) == 100:
        for height in c:
            print(height)
        break


# 투포인터로 제외할 2명 찾기
target = sum(heights) - 100

i, j = 0, len(heights) - 1
while i < j:
    s = heights[i] + heights[j]
    if s == target:
        for k in range(9):
            if k != i and k != j:
                print(heights[k])
        break
    elif s < target:
        i += 1
    else:  # s > target
        j -= 1
