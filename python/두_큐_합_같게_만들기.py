from collections import deque


def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    if sum_q1 == sum_q2:
        return 0

    total = sum_q1 + sum_q2

    if total % 2 == 1:
        return -1

    arr = queue1 + queue2

    if max(arr) > total // 2:
        return -1

    left = 0  # queue1 의 시작
    right = len(queue1) - 1  # queue1 의 끝
    curr = sum(queue1)
    target = total // 2
    count = 0
    n = len(queue1)
    LIMIT = 3 * n + 1

    while count <= LIMIT:
        if curr == target:
            return count
        if curr > target:
            if left > right or left >= 2 * n:
                return -1
            curr -= arr[left]
            left += 1
        else:
            right += 1
            if right >= 2 * n:
                return -1
            curr += arr[right]

        count += 1

    return -1

    # q1 = deque(queue1)
    # q2 = deque(queue2)
    # count = 0
    # while sum_q1 != sum_q2:
    #     if not q1 or not q2:
    #         return -1
    #
    #     if sum_q1 > sum_q2:
    #         pop_q1 = q1.popleft()
    #         q2.append(pop_q1)
    #         sum_q1 -= pop_q1
    #         sum_q2 += pop_q1
    #     else:
    #         pop_q2 = q2.popleft()
    #         q1.append(pop_q2)
    #         sum_q1 += pop_q2
    #         sum_q2 -= pop_q2
    #     count += 1


a = [1, 2, 1, 2]
b = [1, 10, 1, 2]
aa = solution(a, b)
print()
print(aa)
