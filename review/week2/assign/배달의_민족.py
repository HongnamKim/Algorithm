shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()

    for order in orders:
        if not find(menus, order):
            return False
    return True


def find(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return True
        elif array[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
