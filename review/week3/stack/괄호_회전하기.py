def rotate(s):
    head = s[0]
    tail = s[1:]

    return tail + head

def check(s):
    stack = []
    pairs = {")" : "(", "}" : "{", "]" : "["}

    for c in s:
        if c not in pairs:
            stack.append(c)
        else:
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False

    return not stack

def solution(s):
    answer = 0

    for _ in range(len(s)):
        if check(s):
            answer += 1
        s = rotate(s)


    return answer


s = "[](){}"
print(solution(s))