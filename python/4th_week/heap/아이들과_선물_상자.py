import sys
import heapq

input = sys.stdin.readline

# n = 선물 상자 수
# m = 아이들 수
n, m = map(int, input().split(" "))

present = list(map(int, input().split(" ")))
p = [pr * -1 for pr in present]
children = list(map(int, input().split(" ")))
heapq.heapify(p)

answer = 1

for child in children:
    pick = heapq.heappop(p) * -1

    if pick < child:
        answer = 0
        break

    if pick - child > 0:
        heapq.heappush(p, child - pick)


print(answer)
