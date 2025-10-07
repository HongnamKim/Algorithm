def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []

    for a in string:
        if a == "(":
            stack.append(1)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    return True if not stack else False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
