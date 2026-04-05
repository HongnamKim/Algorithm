def solution(n, k):
    arr = list(range(1, n + 1))

    print(arr)

    result = []

    index = k - 1
    while len(arr) > 0:
        result.append(str(arr.pop(index)))
        if len(arr) == 0:
            break
        index = (index + k - 1) % len(arr)

    return result


n, k = map(int, input().split())

result = ", ".join(solution(n, k))

print("<" + result + ">")
