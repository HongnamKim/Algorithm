import sys
import heapq

input = sys.stdin.readline

n = int(input())

meetings = []

for _ in range(n):
    meeting = list(map(int, input().split(" ")))
    meetings.append(meeting)

meetings.sort(key=lambda m: m[0])

rooms = []

room_count = 0
for meeting in meetings:
    if not rooms:
        heapq.heappush(rooms, meeting[1])
        room_count += 1
    elif rooms[0] <= meeting[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, meeting[1])
    else:
        room_count += 1
        heapq.heappush(rooms, meeting[1])

print(room_count)
