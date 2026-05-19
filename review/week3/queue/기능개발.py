import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = []

    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100 - progress) / speed))

    print(days)

    queue = deque()

    for day in days:
        a = 0
        while queue and queue[0] < day:
            queue.popleft()
            a += 1

        queue.append(day)

        if a != 0:
            answer.append(a)
            a = 0

    if queue:
        answer.append(len(queue))

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))