finding_target = 4
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# [0 1 2 3 4 5 6]
def is_exist_target_number_binary(target, array):
    # 이 부분을 채워보세요!
    array.sort()
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    while left <= right:
        if array[mid] > target:
            right = mid - 1
            mid = (left + right) // 2
        elif array[mid] == target:
            return True
        else:
            left = mid + 1
            mid = (left + right) // 2

    return False



result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)