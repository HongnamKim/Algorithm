def solution(s):
    answer = True

    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

    return len(stack) == 0


s = "(()("

print(solution(s))