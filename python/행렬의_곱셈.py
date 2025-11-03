def solution(arr1, arr2):

    n = len(arr1)
    m = len(arr2[0])

    answer = [[] for _ in range(n)]

    for i in range(n):
        prod = 0
        for j in range(m):
            prod = prod + (arr1[i][j] * arr2[j][i])
        answer[i].append(prod)

    return answer


a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]

aa = solution(a, b)
print(aa)
