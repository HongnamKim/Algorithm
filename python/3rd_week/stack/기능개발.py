import math
from collections import deque


def solution(progresses, speeds):
    answer = []

    queue = deque()

    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])

        answer_num = 0

        while queue and queue[0] < day:
            queue.popleft()
            answer_num += 1

        if answer_num > 0:
            answer.append(answer_num)

        queue.append(day)

    answer_num = 0
    while queue:
        queue.popleft()
        answer_num += 1

    answer.append(answer_num)

    return answer


def solution_linear(progresses, speeds):
    data = []  # <-- [(5, 1), (10, 3), (20, 2)]

    for p, s in zip(progresses, speeds):
        if len(data) == 0 or data[-1][0] < -((p - 100) // s):
            data.append([-((p - 100) // s), 1])
        else:
            data[-1][1] += 1

    return [d[1] for d in data]


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
print(solution_linear(progresses, speeds))
