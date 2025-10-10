from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = input()
    x = input()[1:-1]

    x = deque(x.split(","))

    isError = False
    isReversed = False
    for func in p:
        if func == "R":
            isReversed = not isReversed
        else:
            if not x or x[0] == "":
                isError = True
                break
            x.pop() if isReversed else x.popleft()

    if isReversed:
        x.reverse()

    print("error" if isError else "[" + ",".join(x) + "]")
