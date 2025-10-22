import sys

input = sys.stdin.readline

node_count, edge_count = map(int, input().split())

graph = [[] for _ in range(node_count + 1)]

for _ in range(edge_count):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


# def dfs(graph, node, visited_node):
#     visited_node.append(node)
#     for adjacent_node in graph[node]:
#         if adjacent_node not in visited_node:
#             dfs(graph, adjacent_node, visited_node)
#     return


visited = [False] * (node_count + 1)
graph_count = 0

for start_node in range(1, node_count + 1):
    if visited[start_node]:
        continue

    stack = [start_node]
    while stack:
        node = stack.pop()

        if visited[node]:
            continue
        visited[node] = True
        stack = stack + graph[node]

    graph_count += 1

# for start_node in range(1, node_count + 1):
#     if visited[start_node]:
#         continue
#
#     stack = [start_node]
#     while stack:
#         node = stack.pop()
#
#         visited[node] = True
#         for adjacent_node in graph[node]:
#             if not visited[adjacent_node]:
#                 stack.append(adjacent_node)
#
#     graph_count += 1


print(graph_count)
