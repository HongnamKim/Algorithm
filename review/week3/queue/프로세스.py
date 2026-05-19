from collections import deque

def solution(priorities, location):

    queue = deque([index, priority] for index, priority in enumerate(priorities))
    priority_queue = deque(sorted(priorities, reverse=True))

    print(queue)
    print(priority_queue)

    answer = 0
    while True:
        if priority_queue[0] == queue[0][1]:

            answer += 1
            if location == queue[0][0]:
                return answer

            queue.popleft()
            priority_queue.popleft()
        else:
            task = queue.popleft()
            queue.append(task)

priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))