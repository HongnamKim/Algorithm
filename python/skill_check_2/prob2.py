def solution(n, k, enemy):
    """
    병사 n 명
    적: enemy
    """
    round = 0
    for i in range(len(enemy)):

        if enemy[i] > n // 2 and k > 0:
            k -= 1
            round += 1
        else:
            n = n - enemy[i]
            if n < 0:
                break
            round += 1

    return round


a = 7
b = 3
c = [4, 2, 4, 5, 3, 3, 1]
print(solution(a, b, c))
