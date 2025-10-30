from collections import defaultdict


def solution_stack(tickets):
    graph = defaultdict(list)
    for start, to in tickets:
        graph[start].append(to)
    for start in graph:
        graph[start].sort(reverse=True)

    stack = ["ICN"]
    route = []

    while stack:
        print(stack)
        print(graph)
        cur = stack[-1]

        if graph[cur]:
            nxt = graph[cur].pop()
            stack.append(nxt)
        else:
            route.append(stack.pop())

    route.reverse()
    return route


def solution(tickets):
    graph = defaultdict(list)

    for start, to in tickets:
        graph[start].append([to, False])

    for start in graph:
        graph[start].sort()

    n = len(tickets) + 1
    path = ["ICN"]
    results = []

    def dfs():
        if results:
            return

        if len(path) == n:
            results.append(path.copy())
            return

        last_city = path[-1]

        for i in range(len(graph[last_city])):
            if graph[last_city][i][1]:
                continue
            path.append(graph[last_city][i][0])
            graph[last_city][i][1] = True
            dfs()
            path.pop()
            graph[last_city][i][1] = False

    dfs()

    return results[0]


a = [
    ["ICN", "AAA"],
    ["ICN", "CCC"],
    ["CCC", "DDD"],
    ["AAA", "BBB"],
    ["AAA", "BBB"],
    ["DDD", "ICN"],
    ["BBB", "AAA"],
]

# print(solution(a))
print(solution_stack(a))
