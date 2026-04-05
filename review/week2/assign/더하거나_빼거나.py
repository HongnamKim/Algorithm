numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    answer = 0

    def foo(arr, index, sum):
        nonlocal answer
        if index == len(arr):
            # sums.append(sum)
            if sum == target:
                answer += 1
            return

        foo(arr, index + 1, sum + arr[index])
        foo(arr, index + 1, sum - arr[index])

    foo(array, 0, 0)

    return answer


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))

from itertools import product

for signs in product([1, -1], repeat=len(numbers)):
    sum = 0
    for a, b in zip(numbers, signs):
        sum += a * b

    print(sum)
