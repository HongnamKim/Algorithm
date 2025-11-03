def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))

    phone_book_set = set(phone_book)

    if len(phone_book_set) != len(phone_book):
        return False

    for num in phone_book:
        for i in range(1, len(num)):
            if num[0:i] in phone_book_set:
                return False

    return True


def solution2(phone_book):
    phone_book.sort()

    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            return False

    return True


a = ["119", "97674223", "1195524421", "1"]

aa = solution(a)
print(solution2(a))

print()
print(aa)
