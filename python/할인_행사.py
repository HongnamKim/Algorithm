from collections import Counter, defaultdict


def solution(want, number, discount):
    answer = 0

    # wish_list = defaultdict(int)
    #
    # for item, count in zip(want, number):
    #     wish_list[item] = count
    wish_list = Counter(dict(zip(want, number)))

    discount_length = len(discount)
    for start_day in range(0, discount_length - 9):

        discount_items = discount[start_day : start_day + 10]
        buy_list = Counter(discount_items)
        if buy_list == wish_list:
            answer += 1

    return answer


a = ["banana", "apple", "rice", "pork", "pot"]
b = [3, 2, 2, 2, 1]
c = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]

aa = solution(a, b, c)
print()
print(aa)
