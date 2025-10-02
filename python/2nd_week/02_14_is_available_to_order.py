shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def find(menus, order):
    left = 0
    right = len(menus) - 1
    mid = (left + right) // 2

    while left <= right:
        if menus[mid] == order:
            return True
        elif menus[mid] > order:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2

    return False

# binary search
def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()

    for order in orders:
        search_result = find(menus, order)
        if not search_result:
            return False

    return True

# set
def is_available_to_order_improved(menus, orders):
    menu_set = set(menus)

    for order in orders:
        if order not in menu_set:
            return False

    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)

result2 = is_available_to_order_improved(shop_menus, shop_orders)
print(result2)