from functools import cmp_to_key


def cmp(back, front):

    front_pivot = front[0]  # head, number, tail
    back_pivot = back[0]  # head, number, tail

    # head 비교
    if front_pivot[0] > back_pivot[0]:
        return -1
    elif front_pivot[0] < back_pivot[0]:

        return 1
    else:
        # number 비교
        if int(front_pivot[1]) > int(back_pivot[1]):
            print(front_pivot, back_pivot)
            return -1
        elif int(front_pivot[1]) < int(back_pivot[1]):
            return 1
        else:
            return 0


def solution(files):
    sort_files = [()] * len(files)

    for i in range(len(files)):
        file_name = files[i].lower()
        head = ""
        number = ""
        tail = ""

        head_open = True
        number_open = True

        for j, c in enumerate(file_name):
            char_code = ord(c)
            if head_open and (
                65 <= char_code <= 122
                or char_code == 32  #  (공백)
                or char_code == 45  # -
                or char_code == 46
            ):  # .
                head += c
            elif number_open and 48 <= char_code <= 57:
                head_open = False
                number += c
            else:
                number_open = False
                tail += c

        sort_files[i] = ((head, number, tail), i, files[i])
    # print(sort_files)

    result = sorted(sort_files, key=cmp_to_key(cmp))
    # print(result)

    answer = list(map(lambda x: x[2], result))
    return answer


a = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
aa = solution(a)

print()
print(aa)
