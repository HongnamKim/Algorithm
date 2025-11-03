from functools import cmp_to_key


def solution(s):

    s = (s[1 : len(s) - 1].replace("{", "")).split("},")
    s[-1] = s[-1][:-1]

    def cmp(x, y):
        if len(x) > len(y):
            return 1
        else:
            return -1

    s.sort(key=cmp_to_key(cmp))

    check = set()
    answer = []

    for sub_set in s:
        sub_set = map(int, sub_set.split(","))
        for num in sub_set:
            if num not in check:
                check.add(num)
                answer.append(num)

    return answer


a = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
aa = solution(a)

print()
print(aa)
