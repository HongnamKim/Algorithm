n = int(input())

for i in range(n):
    string = input()
    stack = []

    answer = 'YES'
    for j in range(len(string)):

        if string[j] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                answer = 'NO'
                break

            stack.pop()

    if len(stack) != 0:
        answer = 'NO'

    print(answer)


