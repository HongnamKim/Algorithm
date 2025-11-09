from itertools import combinations
from collections import Counter


def is_sub_set(small, big):
    for s in small:
        if s not in big:
            return False
    return True


def solution(orders, course):
    answer = []

    for r in course:
        counter = Counter()
        for order in orders:
            if len(order) < r:
                continue
            s = sorted(order)
            for c in combinations(s, r):
                counter["".join(c)] += 1

        print(counter)
        if counter:
            max_count = max(counter.values())
            for new_course in counter:
                if counter[new_course] >= 2 and counter[new_course] == max_count:
                    answer.append(new_course)

    return sorted(answer)

    # all_menus = set()
    # for order in orders:
    #     for menu in order:
    #         all_menus.add(menu)
    #
    # answer = []
    #
    # for menu_count in course:
    #
    #     menu_counter = Counter()
    #     for c in combinations(all_menus, r=menu_count):
    #         c = sorted(list(c))
    #
    #         for order in orders:
    #             if is_sub_set(c, order):
    #                 new_course = "".join(c)
    #                 menu_counter[new_course] += 1
    #
    #     if menu_counter:
    #         max_count = max(menu_counter.values())
    #
    #         for new_course in menu_counter:
    #             if (
    #                 menu_counter[new_course] >= 2
    #                 and menu_counter[new_course] == max_count
    #             ):
    #                 answer.append(new_course)
    #
    # return sorted(answer)


a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
b = [2, 3, 5]

result = solution(a, b)

print()
print(result)
