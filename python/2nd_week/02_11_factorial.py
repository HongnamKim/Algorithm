def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))

memo = {0: 1, 1: 1}

def dp_factorial(number):
    if number in memo:
        return memo[number]
    else:
        memo[number] = number * dp_factorial(number - 1)
        return memo[number]

print(dp_factorial(5))