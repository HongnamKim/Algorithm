from collections import Counter


def get_intersection(shorter, longer):
    results = []

    shorter_copy = shorter.copy()
    longer_copy = longer.copy()

    for s in shorter_copy:
        if s in longer_copy:
            results.append(s)
            longer_copy.remove(s)

    return results


aa = [1, 1, 2, 2, 3]
bb = [1, 2, 2, 4, 5]
print(get_intersection(aa, bb))


def get_union(shorter, longer):
    intersection = get_intersection(shorter, longer)

    union = shorter + longer

    for s in intersection:
        union.remove(s)

    return union


def solution(str1, str2):
    str1_sep = []
    str2_sep = []

    for i in range(len(str1) - 1):
        sep = str1[i : i + 2].lower()
        check = True
        for c in sep:
            if 97 > ord(c) or 122 < ord(c):
                check = False
                break
        check and str1_sep.append(sep)
    for i in range(len(str2) - 1):
        sep = str2[i : i + 2].lower()
        check = True
        for c in sep:
            if 97 > ord(c) or 122 < ord(c):
                check = False
                break
        check and str2_sep.append(sep)

    s1_len = len(str1_sep)
    s2_len = len(str2_sep)

    shorter = str1_sep if s1_len < s2_len else str2_sep
    longer = str2_sep if s1_len < s2_len else str1_sep

    intersections = get_intersection(shorter, longer)
    union = get_union(shorter, longer)

    answer = (
        int((len(intersections) / len(union)) * 65536) if len(union) != 0 else 1 * 65536
    )
    return answer


def to_bigrams(s):
    s = s.lower()
    out = []
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if a.isalpha() and b.isalpha() and a.isascii() and b.isascii():
            out.append(a + b)
    return out


def solution2(str1, str2):
    c1 = Counter(to_bigrams(str1))
    c2 = Counter(to_bigrams(str2))

    intersection = c1 & c2
    union = c1 | c2

    inter_size = sum(intersection.values())
    union_size = sum(union.values())

    if union_size == 0:
        return 65536
    return int((inter_size / union_size) * 65536)


a = "FRANCE"
b = "french"

aa = solution2(a, b)
print()
print(aa)
