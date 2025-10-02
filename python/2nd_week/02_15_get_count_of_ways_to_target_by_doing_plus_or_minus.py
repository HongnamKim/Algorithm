from itertools import product

numbers =[2, 3, 1] #[1,1,1,1,1]
target_number = 3

l = [(x, -x) for x in numbers] # [(2, -2), (3, -3), (1, -1)]
s = list(map(sum, product(*l))) # 각 튜플에서 하나씩 뽑아서 조합을 만듦
print('s',s.count(target_number))

result = []

def get_all_results(array, current_index, current_sum):
    if current_index >= len(array) - 1:
        result.append(current_sum + array[current_index])
        result.append(current_sum - array[current_index])
        return

    get_all_results(array, current_index + 1, current_sum + array[current_index])
    get_all_results(array, current_index + 1, current_sum - array[current_index])


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    get_all_results(array, 0, 0)

    print('result:', result)

    answer = 0
    for i in result:
        if i == target:
            answer += 1

    return answer


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
