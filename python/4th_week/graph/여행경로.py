from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append([end, False])

    for a in graph:
        graph[a].sort(key=lambda x: x[0], reverse=True)

    print(graph)

    visited = []

    stack = ["ICN"]

    while stack:
        city = stack.pop()

        visited.append(city)

        for i in range(len(graph[city])):
            if not graph[city][i][1]:
                stack.append(graph[city][i][0])
                graph[city][i][1] = True

    return visited


a = [
    ["ICN", "AAA"],
    ["ICN", "CCC"],
    ["CCC", "DDD"],
    ["AAA", "BBB"],
    ["AAA", "BBB"],
    ["DDD", "ICN"],
    ["BBB", "AAA"],
]
print(solution(a))
