import sys
import heapq

input = sys.stdin.readline

# node_count, edge_count = map(int, input().split())
#
# start_node = int(input())
#
# graph = {i: [] for i in range(1, node_count + 1)}
#
# for _ in range(edge_count):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))

node_count, edge_count = 5, 6
start_node = 1
graph = {  #
    1: [(2, 2), (3, 3)],  #
    2: [(3, 4), (4, 5)],  #
    3: [(4, 6)],  #
    4: [],  #
    5: [(1, 1)],  #
}

INF = int(1e9)

# 최단 거리 테이블 초기화
dist = [INF] * (node_count + 1)

# 시작점의 최단거리 0으로 설정
dist[start_node] = 0

# 최소힙으로 다음 탐색 노드 관리
heap = [(0, start_node)]  # (노드까지의 거리, 노드번호)

while heap:
    distance, target_node = heapq.heappop(heap)
    if dist[target_node] < distance:
        continue  # 최단 거리 테이블에 이미 현재까지 최소 거리가 기록되어 있음

    # 노드에서 갈 수 있는 다른 노드들 탐색
    for node, weight in graph[target_node]:
        new_distance = distance + weight
        if dist[node] > new_distance:  # 새로운 최단거리 발견 시
            dist[node] = new_distance  # 최단거리 테이블 갱신
            heapq.heappush(heap, (new_distance, node))  # 다음 탐색을 위한 heap 에 추가

print(dist)
