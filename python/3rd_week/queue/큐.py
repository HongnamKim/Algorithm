from collections import deque

n = int(input())

queue = deque()

for i in range(n):
    command_input = input().split()

    command = command_input[0]

    if len(command_input) == 2:
        num = int(command_input[1])

        if command == "push":
            queue.append(num)

        continue

    if command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if command == "size":
        print(len(queue))

    if command == "empty":
        print(0 if len(queue) else 1)

    if command == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])

    if command == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
