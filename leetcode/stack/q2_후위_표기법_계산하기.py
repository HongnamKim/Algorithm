def evalRPN(tokens):
    stack = []

    operations = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operations:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))


    return stack[0]

t = ["2","1","+","3","*"]
print(evalRPN(t))