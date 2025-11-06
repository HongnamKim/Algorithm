def solution(n):
    board = [[0] * n for _ in range(n)]

    DIRS = ["down", "right", "up"]

    direction = DIRS[0]
    count = 0
    num = 1
    count_limit = (1 + n) * n // 2
    pivot = [0, 0]

    while count < count_limit:
        # 밑으로 이동
        if direction == DIRS[0]:
            start = pivot[0]
            for i in range(start, n):
                if board[i][pivot[1]] != 0:
                    break
                board[i][pivot[1]] = num
                pivot[0] = i
                num += 1
                count += 1

            # 오른쪽으로 방향 전환
            direction = DIRS[1]
            # 오른쪽으로 이동
            pivot[1] += 1

        # 오른쪽으로 이동
        elif direction == DIRS[1]:
            start = pivot[1]
            for j in range(start, n):
                if board[pivot[0]][j] != 0:
                    break
                board[pivot[0]][j] = num
                num += 1
                count += 1
                pivot[1] = j
            direction = DIRS[2]
            pivot[0], pivot[1] = pivot[0] - 1, pivot[1] - 1

        # 위로(대각선) 이동
        else:
            col, row = pivot[0], pivot[1]
            for k in range(n):
                if board[col - k][row - k] != 0:
                    break
                board[col - k][row - k] = num
                num += 1
                count += 1
                pivot[0], pivot[1] = col - k, row - k
            direction = DIRS[0]
            pivot[0] += 1

    answer = []

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                answer.append(board[i][j])

    return answer


a = 6
aa = solution(a)

print()
print(aa)

bb = [
    [1, 0, 0, 0, 0, 0],
    [2, 15, 0, 0, 0, 0],
    [3, 16, 14, 0, 0, 0],
    [4, 17, 21, 13, 0, 0],
    [5, 18, 19, 20, 12, 0],
    [6, 7, 8, 9, 10, 11],
]
