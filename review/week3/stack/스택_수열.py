def stack_sequence(n, sequence):
    stack = []
    stack_num = 1

    answer = []

    for i in range(n):
        while stack_num <= sequence[i]:
            stack.append(stack_num)
            stack_num += 1
            answer.append("+")

        if stack and stack[-1] == sequence[i]:
            stack.pop()
            answer.append("-")
        else:
            return "NO"

    return answer

# sequence = list()
# n = int(input())
# for _ in range(n):
#     sequence.append(int(input()))
n = 3
sequence = [3,1,2]
print(stack_sequence(n, sequence))