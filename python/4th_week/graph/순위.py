def solution(n, results):
    graph = {i: [] for i in range(n + 1)}

    for win, lose in results:
        graph[win].append(lose)

    visited = [[False] * (n + 1) for _ in range(n + 1)]

    print(graph)

    for start_node in range(1, n + 1):
        v = visited[start_node]
        stack = [start_node]

        while stack:
            node = stack.pop()
            v[node] = True

            for next_node in graph[node]:
                if not v[next_node]:
                    stack.append(next_node)
                    v[next_node] = True
        print(start_node, v)


a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(a, b))
