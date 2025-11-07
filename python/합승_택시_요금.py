def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end=" ")
        print()


INF = int(1e9)


def floyd_warshall(matrix):
    """
    플로이드-워셜 알고리즘
    :param matrix: 인접 행렬 (2D list)
    :return: 모든 노드 쌍 간의 최단 거리 dist
    """

    node_count = len(matrix)

    # 거리 테이블 복사 (원본 손상 방지)
    dist = [row[:] for row in matrix]

    for mid_node in range(node_count):
        for start_node in range(node_count):
            # 거쳐갈 수 없는 mid_node 는 스킵
            if dist[start_node][mid_node] >= INF:
                continue
            for end_node in range(node_count):
                new_distance = dist[start_node][mid_node] + dist[mid_node][end_node]

                if new_distance < dist[start_node][end_node]:
                    dist[start_node][end_node] = new_distance

    return dist


def solution(n, s, a, b, fares):

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0

    for start, end, distance in fares:
        graph[start][end] = distance
        graph[end][start] = distance

    # print_graph(graph)
    dist = floyd_warshall(graph)

    total_dist = INF
    for i in range(1, n + 1):
        common_dist = dist[s][i]
        dist1 = dist[i][a]
        dist2 = dist[i][b]
        new_dist = common_dist + dist1 + dist2
        total_dist = min(total_dist, new_dist)

    return total_dist


n = 7  # 노드 개수
s = 3  # 시작 노드
a = 4  # a의 집
b = 1  # b의 집
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

result = solution(n, s, a, b, fares)

print()
print(result)
