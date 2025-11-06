def solution(k, ranges):

    y = [k]
    areas = [0]

    n = 0
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        y.append(k)
        n += 1
        if n > 0:
            areas.append((y[n - 1] + k) / 2)

    # print(y)
    # print(areas)

    answer = []
    for a, b in ranges:
        b = n + b
        if b < a:
            answer.append(-1)
        else:
            answer.append(sum(areas[a + 1 : b + 1]))

    return answer


a = 5
b = [[0, 0], [0, -1], [2, -3], [3, -3]]

aa = solution(a, b)
print()
print(aa)
