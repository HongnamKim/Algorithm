def solution(num, total):
    answer = []
    x = (2 * total - num * (num - 1)) / (2 * num)

    for i in range(num):
        answer.append(x + i)

    return answer


n = 5
t = 5
print(solution(n, t))
