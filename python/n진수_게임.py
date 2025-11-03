def convert(n, k):
    if n == 0:
        return "0"

    result = ""

    alph = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    while n > 0:
        n, mod = divmod(n, k)
        if mod > 9:
            mod = alph[mod]
        result = str(mod) + result

    return result


def solution(n, t, m, p):
    # 진수
    answer = ""

    num = 0
    for _ in range(t * m):
        answer += str(convert(num, n))
        num += 1

    result = ""
    for i in range(p - 1, t * m, m):
        result += answer[i]

    return result


a = 16
b = 16
c = 2
d = 2

aa = solution(a, b, c, d)
print()
print(aa)
