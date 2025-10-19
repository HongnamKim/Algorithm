from collections import deque
import heapq


def solution(jobs):
    request_jobs = [[job[0], job[1], i] for i, job in enumerate(jobs)]

    request_jobs.sort(key=lambda x: x[0])
    # (요청 시점, 소요 시간, 작업 번호)
    request_queue = deque(request_jobs)

    waiting_heap = []
    time = 0
    answer = 0
    job_count = len(request_queue)

    while request_queue:
        if time < request_queue[0][0]:
            time = request_queue[0][0]

        # 현재 시간 이전에 요청 들어온 작업들을 대기 큐에 넣기
        while request_queue and request_queue[0][0] <= time:
            job = request_queue.popleft()
            # (소요시간, 요청시점, 작업번호) 대기큐 우선 순위
            heapq.heappush(waiting_heap, (job[1], job[0], job[2]))

        while waiting_heap:
            current_job = heapq.heappop(waiting_heap)
            time += current_job[0]

            while request_queue and request_queue[0][0] <= time:
                job = request_queue.popleft()
                # (소요시간, 요청시점, 작업번호) 대기큐 우선 순위
                heapq.heappush(waiting_heap, (job[1], job[0], job[2]))

            answer += time - current_job[1]

    return answer // job_count


j = [[0, 3], [1, 9], [3, 5]]
print(solution(j))
