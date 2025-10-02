def solution(n, times):
    low = 1
    high = max(times) * n
    answer = high

    while low <= high:
        mid = (low + high) // 2
        max_n = sum([mid // time for time in times])

        if max_n >= n:
            # 시간 줄이기
            high = mid - 1
            answer = mid
        else:
            # 시간 늘이기
            low = mid + 1

    return answer

print(solution(6, [7, 10]))