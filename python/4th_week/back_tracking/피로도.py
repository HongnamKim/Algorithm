"""
피로도 사용해서 던전 탐험
던전 - 최소 필요 피로도 + 소모 피로도
    최소 필요 피로도 -> 던전 들어가기 위해 갖고 있어야 하는 피로도
    소모 피로도 -> 던전 탐험 후 소모되는 피로도
"""

from itertools import permutations


def solution(k, dungeons):
    n = len(dungeons)

    nums = [i for i in range(n)]

    max_count = 0
    for p in permutations(nums, r=n):
        dungeon_count = 0
        kk = k
        for i in p:
            if kk >= dungeons[i][0]:  # 현재 피로도가 필요 피로도보다 낮으면
                kk -= dungeons[i][1]  # 던전 탐험
                dungeon_count += 1

        max_count = max(max_count, dungeon_count)
        if max_count == n:
            return max_count

    return max_count


def solution2(k, dungeons):
    n = len(dungeons)  # 던전 개수
    used = [False] * n  # 방문한 던전 기록
    best = 0  # 최대 탐험 가능 던전 개수

    def dfs(energy, count):
        nonlocal best  # solution2 의 best 변수 사용
        if (
            count + (n - sum(used)) <= best
        ):  # 남은 모든 던전을 다 돌아도 best 보다 적을 경우 조기 종료
            return

        best = max(best, count)

        for i, (need, cost) in enumerate(dungeons):
            if not used[i] and energy >= need:
                used[i] = True
                dfs(energy - cost, count + 1)
                used[i] = False

    dfs(k, 0)
    return best


def solution_back_tracking(k, dungeons):
    answer = 0

    n = len(dungeons)
    visited = [False] * n

    def dfs(energy, count):
        nonlocal answer
        if answer > count + (n - sum(visited)):
            return

        answer = max(count, answer)

        for i in range(n):
            cost = dungeons[i][1]
            need = dungeons[i][0]
            if energy >= need and not visited[i]:
                visited[i] = True
                dfs(energy - cost, count + 1)
                visited[i] = False

    dfs(k, 0)

    return answer


a = 80
b = [[80, 20], [50, 40], [30, 10]]
print(solution(a, b))
print(solution2(a, b))
print(solution_back_tracking(a, b))
