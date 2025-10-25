def solution(n):
    moves = []

    def hanoi(k, src, aux, dst):
        if k == 0:
            return
        # 1) 위의 k-1개를 보조기둥(aux)로
        hanoi(k - 1, src, dst, aux)
        # 2) 가장 큰 원판 1개를 목적기둥(dst)로
        moves.append([src, dst])
        # 3) 보조기둥에 있던 k-1개를 목적기둥(dst)로
        hanoi(k - 1, aux, src, dst)

    hanoi(n, 1, 2, 3)
    return moves


a = 2
print(solution(a))
