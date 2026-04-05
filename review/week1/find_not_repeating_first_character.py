input = "abadabac"


def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    arr = [0] * 26  # 각 알파벳 빈도

    for char in string:
        index = ord(char) - ord("a")
        arr[index] += 1

    alph = []
    for i in range(len(arr)):
        if arr[i] == 1:
            alph.append(chr(i + ord("a")))

    for char in string:
        if char in alph:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))
