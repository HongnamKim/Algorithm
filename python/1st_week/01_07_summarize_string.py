from xml.etree.ElementTree import tostring


def summarize_string(input_str):
    # 이 부분을 채워보세요!
    count_arr = [0] * 26
    for char in input_str:
        count_arr[ord(char) - ord('a')] += 1

    result = ''
    #print(count_arr)
    for i in range(len(count_arr)):
        if count_arr[i] > 0:
            result = result + chr(i + ord('a')) + str(count_arr[i]) + '/'



    return result[0:-1]

input_str = "aaabbbc"

print(summarize_string(input_str))