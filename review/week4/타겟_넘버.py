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

n = [1,1,1,1,1]
t = 3
print(solution(n, t))