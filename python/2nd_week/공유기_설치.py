from sys import stdin

pos_count, count = map(int, input().split(' '))
pos = [int(y) for y in stdin.read().splitlines()]

#pos_count = 5
#count = 3
#pos = [1, 2, 8, 4, 9]

# count 개수의 공유기를 d 이상의 거리로 설치할 수 있는지
def can(d: int) -> bool:
    cnt = 1
    last = pos[0]
    for i in range(1, pos_count):
        if pos[i] - last >= d:
            cnt += 1
            last = pos[i]
            if cnt >= count:
                return True

    return False

def solution(pos):
    pos.sort()

    low = 1 # 최소 간격
    high = pos[-1] - pos[0] # 최대 간격
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if can(mid): # mid 의 간격으로 설치 가능하면 더 넓혀보기
            low = mid + 1
            answer = mid
        else:
            high = mid - 1

    return answer


print(solution(pos))