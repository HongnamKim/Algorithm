from collections import deque
from functools import cmp_to_key

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

"""
상품의 가격 배열 (prices)
쿠폰 할인율 배열 (coupons, % 단위)

이 때 최대한 할인을 많이 받는다면 얼마를 내야하는가?

전략
1. prices 와 coupons 를 정렬
2. 가장 높은 price 와 가장 큰 할인율을 갖는 coupon 을 짝지음
3. 그때 가격의 총합을 구함
"""


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    total_price = 0

    price_queue = deque(prices)
    coupon_queue = deque(coupons)

    while price_queue and coupon_queue:
        price = price_queue.popleft()
        coupon = coupon_queue.popleft()

        discount_amount = (100 - coupon) / 100

        total_price += price * discount_amount

    while price_queue:
        price = price_queue.popleft()

        total_price += price

    return int(total_price)


print(
    "정답 = 926000 / 현재 풀이 값 = ",
    get_max_discounted_price([30000, 2000, 1500000], [20, 40]),
)
print(
    "정답 = 485000 / 현재 풀이 값 = ",
    get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]),
)
print(
    "정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [])
)
print(
    "정답 = 1458000 / 현재 풀이 값 = ",
    get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]),
)
