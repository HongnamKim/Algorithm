import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# heap 에 supplies 를 넣어둔 다음 가장 많은 재고들을 꺼내서 stock 에 추가
# 현재 재고가 바닥나는 시점 이전까지
#   stock = 10 --> 10일까지는 버틸 수 있음, 11일부터는 불가능
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    last_date_index = 0
    max_heap = []

    while stock <= k:
        # 현재 stock 으로 견딜 수 있는 날짜들만 heap 에 넣기
        # stock = 10
        # dates = [1, 7, 11]
        # supplies = [10, 20, 300]
        while last_date_index < len(dates) and dates[last_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_date_index] * -1)  # [-20, -10]
            last_date_index += 1

        supply = heapq.heappop(max_heap) * -1
        stock += supply
        answer += 1

    return answer


print(
    get_minimum_count_of_overseas_supply(
        ramen_stock, supply_dates, supply_supplies, supply_recover_k
    )
)
print(
    "정답 = 2 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30),
)
print(
    "정답 = 4 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40),
)
print(
    "정답 = 1 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11),
)
