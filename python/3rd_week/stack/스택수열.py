def stack_sequence(n, sequence):
    stack, stack_num = [], 1

    answer = []

    for i in range(n):
        # sequence[i] == 3 일 때 stack [1, 2, 3]
        while stack_num <= sequence[i]:
            stack.append(stack_num)
            stack_num += 1
            answer.append("+")

        if stack and stack[-1] == sequence[i]:
            stack.pop()
            answer.append("-")
        else:
            return "NO"

    # while True:
    #     if stack:
    #         num = stack[-1]
    #         if sequence[i] < num:  # stack 에 있는 숫자가 더 크면 만들 수 없음
    #             return "NO"
    #         elif sequence[i] == num:  # stack 에 있는 숫자가 가능할 경우
    #             answer.append("-")
    #             stack.pop()
    #             break
    #         else:  # stack 에 숫자가 아직 sequence 숫자에 도달하지 않음
    #             stack.append(stack_num)
    #             stack_num += 1
    #             answer.append("+")
    #     else:  # stack 이 비었을 경우 채워넣기
    #         stack.append(stack_num)
    #         answer.append("+")
    #         stack_num += 1

    return "\n".join(answer)


sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))

print(stack_sequence(n, sequence))
