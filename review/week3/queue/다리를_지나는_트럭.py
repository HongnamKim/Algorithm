from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    on_bridge_weight = 0
    on_bridge_trucks = deque([0] * bridge_length)

    while trucks:
        #print(on_bridge_trucks, on_bridge_weight, answer, trucks)
        remove_weight = on_bridge_trucks.popleft()
        on_bridge_weight -= remove_weight

        # 다리에 올라갈 수 있는 경우
        if on_bridge_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            on_bridge_trucks.append(truck)
            on_bridge_weight += truck
        else:
            on_bridge_trucks.append(0)

        answer += 1

    while on_bridge_trucks:
        on_bridge_trucks.popleft()
        answer += 1


    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))