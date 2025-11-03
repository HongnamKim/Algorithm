from collections import defaultdict, Counter, deque


def solution(topping):
    n = len(topping)
    c = Counter(topping)
    front_toppings = defaultdict()
    back_toppings = defaultdict(int, c)

    front = deque(topping[:0])
    back = deque(topping[0:])

    answer = 0

    for i in range(n):
        move_topping = back.popleft()
        front.append(move_topping)

        if move_topping in front_toppings:
            front_toppings[move_topping] += 1
        else:
            front_toppings[move_topping] = 1

        if back_toppings[move_topping] == 1:
            del back_toppings[move_topping]
        else:
            back_toppings[move_topping] -= 1

        if len(front_toppings) == len(back_toppings):
            answer += 1

    return answer


a = [1, 2, 1, 3, 1, 4, 1, 2]
aa = solution(a)

print()
print(aa)
