import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

# print(n, m)
# print(cards)

heapq.heapify(cards)

for _ in range(m):
    card_1 = heapq.heappop(cards)
    card_2 = heapq.heappop(cards)

    new_card = card_1 + card_2

    heapq.heappush(cards, new_card)
    heapq.heappush(cards, new_card)

# print(cards)
print(sum(cards))
