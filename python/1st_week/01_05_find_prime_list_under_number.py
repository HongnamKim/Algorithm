import math

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    result = []

    for num in range(2, number + 1, 1):
        if is_prime_number(num):
            result.append(num)

    return result

def is_prime_number(number):
    for div in range (2, number, 1):
        if number % div == 0:
            return False
    return True

input = 20
result = find_prime_list_under_number(input)
print(result)