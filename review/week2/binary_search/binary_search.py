finding_target = 4
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    left = 0
    right = len(array) - 1

    array.sort()
    print(array)

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
