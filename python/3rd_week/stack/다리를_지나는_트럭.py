from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    queue = deque()

    for truck_weight in truck_weights:
        if len(queue) < bridge_length and sum(queue) + truck_weights[1] <= weight:
            queue.append(truck_weight)

    print(queue)

    return answer


a = 2
b = 10
c = [7, 4, 5, 6]

print(solution(a, b, c))
