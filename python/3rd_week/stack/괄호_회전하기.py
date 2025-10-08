def check_correct(string):
    stack = []

    for s in string:
        if s == "(" or s == ")":
            if s == "(":
                stack.append("(")
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

        elif s == "{" or s == "}":
            if s == "{":
                stack.append("{")
            else:
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        else:
            if s == "[":
                stack.append("[")
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

    if stack:
        return False

    return True


def rotate(string):
    front = string[0]
    tail = string[1:]

    return tail + front


def solution(string):
    answer = 0

    for i in range(len(string)):
        string = rotate(string)

        if check_correct(string):
            print(string)
            answer += 1

    return answer


s = "([)]"
print(solution(s))
