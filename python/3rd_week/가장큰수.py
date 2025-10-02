from functools import cmp_to_key

def solution(array):
    strs = list(map(str, array))

    strs.sort(key=lambda x: x*4, reverse=True)

    # def cmp(a, b):
    #     if a + b > b + a: #330 303
    #         return -1
    #     if a + b < b + a:
    #         return 1
    #     return 0
    #
    # strs.sort(key=cmp_to_key(cmp))
    answer = ''.join(strs)
    return '0' if answer[0] == '0' else answer

numbers = [3, 30, 34, 5, 9]

print(solution(numbers))