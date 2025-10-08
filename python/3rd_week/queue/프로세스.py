from collections import deque
from functools import cmp_to_key


def solution(priorities, location):
    answer = 0

    queue = deque([idx, priority] for idx, priority in enumerate(priorities))

    sorted_queue = deque(sorted(priorities, reverse=True))

    while True:
        if queue[0][1] == sorted_queue[0]:
            answer += 1

            if queue[0][0] == location:
                return answer

            sorted_queue.popleft()
            queue.popleft()
        else:
            queue.rotate(-1)


a = [1, 1, 9, 1, 1, 1]
b = 0

print(solution(a, b))
