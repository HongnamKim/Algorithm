import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = []
for _ in range(n):
    lecture = list(map(int, input().split(" ")))
    lectures.append(lecture)

# print(lectures)

# 시작 시간으로 정렬
lectures.sort(key=lambda x: x[0])

room = []

room_count = 0
for lecture in lectures:
    if not room:
        heapq.heappush(room, lecture[1])
        room_count += 1
    elif room[0] <= lecture[0]:
        heapq.heappop(room)
        heapq.heappush(room, lecture[1])
    else:
        heapq.heappush(room, lecture[1])
        room_count += 1

print(room_count)
