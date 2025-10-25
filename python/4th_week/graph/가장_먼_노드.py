import heapq

INF = int(1e9)


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    start_node = 1
    dist = [INF] * (n + 1)
    heap = [(0, start_node)]
    dist[start_node] = 0

    while heap:
        distance, node = heapq.heappop(heap)
        if dist[node] < distance:
            continue

        for next_node in graph[node]:
            new_distance = distance + 1
            if dist[next_node] > new_distance:
                dist[next_node] = new_distance
                heapq.heappush(heap, (new_distance, next_node))

    max_distance = 0

    answer = 0
    for i in range(1, n + 1):
        if max_distance < dist[i]:
            max_distance = dist[i]
            answer = 1
        elif max_distance == dist[i]:
            answer += 1
        else:
            continue

    return answer


a = 6
b = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(a, b))
