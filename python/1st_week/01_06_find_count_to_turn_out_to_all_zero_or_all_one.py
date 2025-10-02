#input:str = '001100001'
input = input()

def find_count_to_turn_out_to_all_zero_or_all_one(string: str) -> int:
    # 이 부분을 채워보세요!
    first = string[0]
    flag = string[0]
    count = 0

    for i in range(1, len(string), 1):
        if flag != string[i]:
            if string[i] != first:
                count += 1
            flag = string[i]

    return count

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)