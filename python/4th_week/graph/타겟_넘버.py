from itertools import product


def solution(numbers, target):
    n = len(numbers)
    count = 0
    stack = [(0, 0)]

    while stack:
        i, s = stack.pop()
        if i == n:
            if s == target:
                count += 1
            continue
        x = numbers[i]
        stack.append((i + 1, s + x))
        stack.append((i + 1, s - x))

    return count


def solution2(numbers, target):
    # sols = []
    answer = 0
    for signs in product([1, -1], repeat=len(numbers)):
        s = sum(a * b for a, b in zip(numbers, signs))
        if s == target:
            answer += 1

    return answer


a = [4, 1, 2, 1]
b = 4
print(solution2(a, b))

answer = 0
for signs in product((1, -1), repeat=len(a)):
    sum = 0
    for num, sign in zip(a, signs):
        sum += num * sign
    if sum == b:
        answer += 1

print(answer)
