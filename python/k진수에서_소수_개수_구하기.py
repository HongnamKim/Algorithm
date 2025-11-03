import math


def convert(n, k):
    result = ""

    while n > 0:
        n, mod = divmod(n, k)
        result = str(mod) + result

    return result


def check(num):
    if num == 0 or num == 1:
        return False

    end = int(math.sqrt(num))

    for i in range(2, end + 1):
        if num % i == 0:
            return False

    return True


def solution(n, k):
    convert_n = list(map(int, filter(lambda x: x != "", convert(n, k).split("0"))))

    answer = 0

    for n in convert_n:
        if check(n):
            answer += 1

    return answer


a = 110011
b = 10

aa = solution(a, b)

print()
print(aa)
