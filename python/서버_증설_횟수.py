import math
from collections import deque


def solution(players, m, k):
    server = deque()

    answer = 0
    server_count = 0
    for time, player in enumerate(players):
        # 시간 다 된 서버 종료
        while server and time - server[0][0] >= k:
            start_time, shutdown_count = server.popleft()
            server_count -= shutdown_count

        # 현재 플레이어 수를 감당할 수 있는 서버의 수
        required_server_count = math.ceil((player - m + 1) / m)
        if required_server_count > server_count:
            # 추가할 서버 개수
            new_server_count = required_server_count - server_count

            server_count += new_server_count
            answer += new_server_count
            server.append((time, new_server_count))

        # print(player, required_server_count, server_count, answer)

    return answer


a = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
b = 3
c = 5

result = solution(a, b, c)
print()
print(result)
