import heapq

INF = int(1e9)


def solution(N, road, K):
    # N: 노드 개수
    # road: 간선 정보
    # K: 제한 시간
    # 1번 노드에서 K 시간 내에 도달할 수 있는 노드의 개수
    # 다익스트라로 1번 노드에서 다른 노드들까지의 최단 거리 계산

    # road 를 인접리스트로 변환
    graph = {i: [] for i in range(1, N + 1)}
    for start, end, weight in road:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    start_node = 1

    dist = [INF] * (N + 1)
    heap = [(0, start_node)]
    dist[start_node] = 0

    while heap:
        distance, node = heapq.heappop(heap)
        if distance > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_distance = distance + weight
            if dist[next_node] > new_distance:
                dist[next_node] = new_distance
                heapq.heappush(heap, (new_distance, next_node))

    answer = 0

    for distance in dist:
        if distance <= K:
            answer += 1

    return answer


a = 5
b = [  # 양방향 그래프
    [1, 2, 1],  # 1번에서 2번까지 거리 1
    [2, 3, 3],  # 2번에서 3번까지 거리 3
    [5, 2, 2],  # 5번에서 2번까지 거리 2
    [1, 4, 2],  # 1번에서 4번까지 거리 2
    [5, 3, 1],  # 5번에서 3번까지 거리 1
    [5, 4, 2],  # 5번에서 4번까지 거리 2
]
c = 3
print(solution(a, b, c))
