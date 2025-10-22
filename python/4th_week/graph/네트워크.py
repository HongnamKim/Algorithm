def init_graph(n, computers):
    graph = [[] for _ in range(n + 1)]

    for i in range(n):
        adjacent_graph = computers[i]
        for j, node in enumerate(adjacent_graph):
            if i == j:
                continue
            elif node == 1:
                graph[i + 1].append(j + 1)
                # graph[j + 1].append(i + 1)

    return graph


def solution(n, computers):
    graph = init_graph(n, computers)

    answer = 0
    visited = [False] * (n + 1)

    for node in range(1, n + 1):
        if visited[node]:
            continue

        stack = [node]
        while stack:
            node = stack.pop()
            visited[node] = True
            for nxt in graph[node]:
                if not visited[nxt]:
                    stack.append(nxt)
                    visited[nxt] = True
        answer += 1

    return answer


a = 3
b = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(a, b))
