def summarize_string(input_str):
    alph_count = ord("z") - ord("a") + 1

    counter = [0] * alph_count

    for char in input_str:
        index = ord(char) - ord("a")
        counter[index] += 1

    result_arr = []

    for i in range(len(counter)):
        if counter[i] != 0:
            result_arr.append(chr(i + ord("a")) + str(counter[i]))

    return "/".join(result_arr)


input_str = "acccdeee"
print(summarize_string(input_str))
