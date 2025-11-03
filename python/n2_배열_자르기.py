def solution(n, left, right):
    answer = []

    for x in range(left, right + 1):
        i = x // n
        j = x % n
        num = i + 1 if i == j else max(i, j) + 1
        answer.append(num)

    return answer


a = 3
b = 2
c = 5

aa = solution(a, b, c)
print(aa)
