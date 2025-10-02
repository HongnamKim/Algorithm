input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    count_arr = [0] * len('abcdefghijklmnopqrstuvwxyz')

    for char in string:
        if not char.isalpha():
            continue
        count_arr[ord(char) - ord('a')] += 1

    # 한 번만 나온 알파벳
    not_repeating_character_arr = []
    for index in range(len(count_arr)):
        if count_arr[index] == 1:
            not_repeating_character_arr.append(chr(index + ord('a')))

    for char in string:
        if char in not_repeating_character_arr:
            return char

    return '_'


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))