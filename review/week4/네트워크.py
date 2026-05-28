def init_graph(n, c):
    graph = {i: [] for i in range(1, n + 1)}

    for i in range(n):
        computer = c[i]
        for j in range(len(computer)):
            if i == j:
                continue
            if computer[j] == 1:
                graph[i+1].append(j+1)

    return graph

def solution(n, computers):
    graph = init_graph(n, computers)

    answer = 0
    visited = [False] * (n + 1)

    for node in graph:

        if visited[node]: # 다른 노드랑 연결돼서 이미 탐색했던 것은 스킵
            continue

        stack = [node]
        while stack:
            current_node = stack.pop()
            visited[current_node] = True
            for next_node in graph[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)

        answer += 1

    return answer

n = 3
c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, c))