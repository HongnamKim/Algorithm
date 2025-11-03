def solution(msg):
    answer = []

    index = {chr(i): i - 64 for i in range(65, 91)}

    last_index = 26
    max_index_key_length = 1

    while msg:

        for index_length in range(max_index_key_length, -1, -1):
            start = msg[:index_length]
            if start in index.keys():
                answer.append(index[start])
                remove_length = index_length
                msg = msg[remove_length:]
                if msg:
                    new_index = start + msg[0]

                last_index += 1
                index[new_index] = last_index

                max_index_key_length = max(len(new_index), max_index_key_length)
                break

    # print(msg)
    # print(index)

    return answer


a = "ABABABABABABABAB"

aa = solution(a)
print()
print(aa)
