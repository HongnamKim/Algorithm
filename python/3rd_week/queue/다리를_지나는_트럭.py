from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0] * bridge_length)
    bridge_weights = 0
    waiting_trucks = deque(truck_weights)

    truck_count = len(truck_weights)
    arrived_trucks = deque()

    while len(arrived_trucks) < truck_count:
        pop = bridge.popleft()
        if pop != 0:
            arrived_trucks.append(pop)
            bridge_weights -= pop

        if waiting_trucks and bridge_weights + waiting_trucks[0] <= weight:
            new_truck = waiting_trucks.popleft()
            bridge_weights += new_truck
            bridge.append(new_truck)
        else:
            bridge.append(0)

        answer += 1

    return answer


a = 100
b = 100
c = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(a, b, c))
