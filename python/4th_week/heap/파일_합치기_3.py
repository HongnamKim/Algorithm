import sys
import heapq

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    files = list(map(int, input().split(" ")))
    heapq.heapify(files)

    answer = 0

    # 합칠 파일이 2개 이상일 때까지
    while len(files) > 1:
        file_1 = heapq.heappop(files)
        file_2 = heapq.heappop(files)

        resource = file_1 + file_2

        answer += resource
        heapq.heappush(files, resource)

    print(answer)
