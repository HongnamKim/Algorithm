input = 20


def is_prime_num(number):

    for div in range(2, number):
        if div * div <= number and (number % div) == 0:
            return False
    return True


def find_prime_list_under_number(number):
    result = []
    for num in range(2, number + 1):
        if is_prime_num(num):
            result.append(num)

    return result


result = find_prime_list_under_number(input)
print(result)
