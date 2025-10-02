def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num

print(find_max_num([6, 9 ,2, 7, 1888]))