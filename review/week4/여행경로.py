from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, to in tickets:
        graph[start].append(to)
    for start in graph:
        graph[start].sort(reverse=True)

    print(graph)

    stack = ["ICN"]
    visited = []

    while stack:
        curr = stack[-1]

        if graph[curr]:
            nxt = graph[curr].pop()
            stack.append(nxt)
        else:
            visited.append(stack.pop())

    visited.reverse()
    return visited


t =[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))