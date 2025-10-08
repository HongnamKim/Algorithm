from collections import deque

length, term = map(int, input().split())

queue = deque(range(1, length + 1))

answer = []

while queue:
    # for _ in range(term - 1):
    #     queue.append(queue.popleft())
    queue.rotate(-(term - 1))

    answer.append(str(queue.popleft()))

print("<" + ", ".join(answer) + ">")
