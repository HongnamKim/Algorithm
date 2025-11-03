from collections import deque


def solution(elements):
    n = len(elements)

    results = set()

    for length in range(1, n + 1):
        i = 0
        j = i + length - 1  # 0 + 4 - 1

        new_sum = sum(elements[i : j + 1])
        results.add(new_sum)
        while i != n - 1:
            j += 1
            if j >= n:
                j -= n
            new_sum = new_sum - elements[i] + elements[j]
            i += 1
            results.add(new_sum)

    return len(results)


a = [7, 9, 1, 1, 4]

print(solution(a))
