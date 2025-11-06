def search(board, n, answer):
    length = len(board)  # length: 8
    term = length // n  # n: 1, 2, 4, 8... n 등분
    # term: 8, 4, 2, 1...
    for i in range(0, length, term):
        for j in range(0, length, term):
            if board[i][j] != 0 and board[i][j] != 1:
                continue
            compress(board, i, j, term, answer)


def compress(board, i, j, term, answer):
    num = board[i][j]
    is_checked = True

    for x in range(i, i + term):
        for y in range(j, j + term):
            if board[x][y] != num:
                is_checked = False

    if is_checked:
        answer[num] = answer[num] - term * term + 1

        for x in range(i, i + term):
            for y in range(j, j + term):
                board[x][y] = 2

    return is_checked


def init(board):
    count_0 = 0
    count_1 = 0
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count_1 += 1
            else:
                count_0 += 1

    return [count_0, count_1]


def solution(arr):
    answer = init(arr)

    i = 1
    while i < len(arr):
        search(arr, i, answer)
        i *= 2

    return answer


a = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
]

aa = solution(a)
print()
print(aa)
