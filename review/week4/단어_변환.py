

def possible(before, after):
    diff = 0
    for a, b in zip(before, after):
        if a != b:
            diff += 1
            if diff > 1:
                return False

    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    least_count = float('inf')
    stack = [(0, begin, set())] # count, word, visited

    while stack:
        # print(stack)
        count, word, visited = stack.pop()

        if word == target:
            least_count = min(least_count, count)
            continue

        for next_word in words:
            if next_word in visited:
                continue
            if possible(word, next_word):
                # visited.add(next_word)
                stack.append((count + 1, next_word, visited | {next_word}))


    return least_count if least_count != float('inf') else 0

from collections import deque

def bfs_solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(0, begin)])
    visited = {begin}

    while queue:
        count, word = queue.popleft()

        if word == target:
            return count

        for next_word in words:
            if next_word in visited:
                continue
            if possible(word, next_word):
                visited.add(next_word)
                queue.append((count + 1, next_word))

    return 0

b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(b,t,w))
print(bfs_solution(b,t,w))