def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    for alph in string:
        if not alph.isalpha():
            continue
        index = ord(alph) - ord('a')
        alphabet_occurrence_array[index]+=1

    max_index = find_max_num(alphabet_occurrence_array)

    return chr(max_index + ord('a'))

def find_max_num(arr):
    max_index=0
    for index in range(len(arr)):
        if arr[max_index] < arr[index]:
            max_index = index

    return max_index


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))