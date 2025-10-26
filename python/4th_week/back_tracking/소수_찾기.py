import math
from collections import Counter
from itertools import permutations


def is_prime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    n = len(numbers)

    prime_numbers = set()

    for i in range(1, n + 1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            if is_prime(num):
                prime_numbers.add(num)

    return len(prime_numbers)


a = "123"
# print(solution(a))

numbers = [1, 3, 2]


nums = sorted(numbers)
n = len(nums)
used = [False] * len(numbers)
path = []
out = []


def dfs():
    if len(path) == n:
        out.append(int("".join(map(str, path))))  # 3자리 완성, 결과물 out에 추가
        return
    for i in range(n):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        used[i] = True
        path.append(nums[i])
        dfs()
        path.pop()
        used[i] = False


dfs()
print(out)
