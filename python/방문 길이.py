def print_board(board):
    for i in range(len(board)):
        print(board[i])


def solution(dirs):
    answer = 0
    history = set()

    board = [[0] * 11 for _ in range(11)]

    x = 5
    y = 5
    board[y][x] = 1

    for dir in dirs:
        new_x = x
        new_y = y
        if dir == "U":
            new_y -= 1
        elif dir == "D":
            new_y += 1
        elif dir == "L":
            new_x -= 1
        elif dir == "R":
            new_x += 1

        # 경계 넘어가면 무시
        if 0 > new_x or new_x > 10 or 0 > new_y or new_y > 10:
            continue

        edge = (min((x, y), (new_x, new_y)), max((x, y), (new_x, new_y)))

        if edge not in history:
            answer += 1
            history.add(edge)

        board[new_y][new_x] += 1
        x = new_x
        y = new_y

    print_board(board)

    return answer


a = "ULURRDLLU"
aa = solution(a)

print()
print(aa)
