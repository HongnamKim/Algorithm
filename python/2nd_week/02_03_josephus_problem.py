# BOJ 1158

def josephus_problem(n, k):
    # 이 부분을 채워보세요!
    arr = list(range(1, n + 1, 1))

    result = []
    index = k - 1
    while len(arr) > 0:
        result.append(str(arr.pop(index)))

        if len(arr) == 0:
            break

        index = (index + k - 1) % len(arr)
    return result

n, k = map(int, input().split())
result = ', '.join((josephus_problem(n, k)))
print('<' + result + '>')