from collections import deque


def solution(n, m, arr):
    answer = 0

    queue = deque(range(1, n + 1))

    i = 0
    count = 0

    while True:
        # print(queue, answer, queue[len(queue) // 2])
        if queue[0] == arr[i]:
            queue.popleft()
            i += 1
            count += 1
            if count == m:
                break
        else:
            for j in range(len(queue)):
                if queue[j] == arr[i]:
                    if j > len(queue) // 2:
                        queue.rotate(1)
                        answer += 1
                    else:
                        queue.rotate(-1)
                        answer += 1
                    break

    return answer


# n = 10  # <= 50, 큐의 크기
# m = 10  # <= n, 뽑아내려고 하는 수의 개수
# arr = [1, 6, 3, 2, 7, 9, 8, 4, 10, 5]

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(n, m, arr))
