def solution(n, wires):
    answer = n

    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            node_1, node_2 = wires[j]
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)

        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        while stack:
            node = stack.pop()
            for nxt_node in graph[node]:
                if visited[nxt_node]:
                    continue
                stack.append(nxt_node)
                visited[nxt_node] = True

        diff = abs(n - 2 * sum(visited))
        if diff == 0:
            return 0
        else:
            answer = min(diff, answer)

    return answer


a = 4
b = [[1, 2], [2, 3], [3, 4]]
print(solution(a, b))
