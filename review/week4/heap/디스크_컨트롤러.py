import heapq
from collections import deque

def solution(jobs):
    job_count = len(jobs) # 작업 개수
    time = 0 # 현재 시간
    # 작업시간, 요청 시각, 작업 번호 순서
    jobs = sorted([(duration, call, index) for index, (call, duration) in enumerate(jobs)], key=lambda x: x[1])
    jobs = deque(jobs)

    queue = []

    # 반환 시간
    total_return_time = 0

    while jobs:
        if time >= jobs[0][1]:
            # 요청 작업 중 현재 시간 이전에 들어온 작업들을 큐에 넣기
            while jobs and jobs[0][1] <= time:
                heapq.heappush(queue, jobs.popleft())

            while queue:
                duration, call, index = heapq.heappop(queue)
                time += duration
                while jobs and jobs[0][1] <= time:
                    heapq.heappush(queue, jobs.popleft())
                total_return_time += (time - call)
        else: # time < jobs[0][1] -> 작업이 들어올때의 시간으로 이동
            time = jobs[0][1]

        print(time)

    return total_return_time // job_count


j =  [[0,1],[0,10],[1,2],[1,1]]
print(solution(j))