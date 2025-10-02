def can(rocks, d, n):
    cnt = 0
    last = 0
    removed = []
    print('mid: ', d)

    for i in range(1, len(rocks)):
        if rocks[i] - last >= d:
            print(rocks[i])
            cnt += 1
            last = rocks[i]
            removed.append(last)
            if cnt >= n:
                print(removed)
                return True

    return False

def solution(distance, rocks, n):
    rocks.sort()

    low = min(rocks)
    high = max(distance - rocks[-1], rocks[-1])

    print(low)
    print(high)
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if can(rocks, mid, n):
            low = mid + 1
            answer = mid
        else:
            high = mid - 1

    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance, rocks, n))