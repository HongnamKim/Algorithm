def print_board(m, n, board):
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

    print()


def search(m, n, board):
    is_search = False
    for i in range(m - 1):
        for j in range(n - 1):
            curr = board[i][j].lower()
            if "a" > curr or "z" < curr:
                continue

            right = board[i][j + 1].lower()
            under = board[i + 1][j].lower()
            diag = board[i + 1][j + 1].lower()

            if curr == right == under == diag:
                is_search = True
                check = curr.lower()
                board[i][j] = check
                board[i][j + 1] = check
                board[i + 1][j] = check
                board[i + 1][j + 1] = check

    return is_search


def erase(m, n, board):
    count = 0

    for i in range(m):
        for j in range(n):
            if "a" <= board[i][j] <= "z":
                count += 1
                board[i][j] = "-"

    return count


def move(m, n, board):
    key = True
    while key:
        is_moved = False
        for i in range(m - 1):
            for j in range(n):
                curr = board[i][j]
                under = board[i + 1][j]
                if under == "-" and curr != "-":
                    is_moved = True
                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

        if not is_moved:
            key = False


def solution(m, n, board):
    b = [[""] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            b[i][j] = board[i][j]

    print_board(m, n, b)

    answer = 0
    while True:
        is_searched = search(m, n, b)
        answer += erase(m, n, b)
        # print_board(m, n, b)

        move(m, n, b)
        # print_board(m, n, b)

        if not is_searched:
            break

    return answer


a = 4
b = 5
c = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

solution(a, b, c)
