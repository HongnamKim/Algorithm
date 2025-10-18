import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

answer = 0

while len(cards) > 1:
    card_1 = heapq.heappop(cards)  # 최소값
    card_2 = heapq.heappop(cards)  # 2번째 최소값

    new_card = card_1 + card_2

    answer += new_card
    heapq.heappush(cards, new_card)
    # print(cards)

# print(cards)
print(answer)
