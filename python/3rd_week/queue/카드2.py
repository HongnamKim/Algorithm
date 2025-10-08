from collections import deque

# n = int(input())

n = 6

cards = deque([n for n in range(1, n + 1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
