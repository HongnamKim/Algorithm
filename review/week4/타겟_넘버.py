answers = []

def sub_solution(numbers, target, total, index):
    if index == len(numbers):
        if total == target:
            answers.append(total)
        return
    else:
        sub_solution( numbers, target, total + numbers[index], index + 1)
        sub_solution(numbers, target, total - numbers[index], index + 1)


def solution(numbers, target):
    sub_solution( numbers, target, 0, 0)

    return len(answers)

def stack_solution(numbers, target):
    count = 0
    stack = [(0, 0)] # index, sum

    while stack:
        index, sum = stack.pop()
        if index == len(numbers):
            if sum == target:
                count += 1
            continue

        x = numbers[index]
        stack.append((index + 1, sum + x))
        stack.append((index + 1, sum - x))

    return count

n = [1,1,1,1,1]
t = 3
print(solution(n, t))
print(stack_solution(n, t))