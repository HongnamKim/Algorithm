def buildArray(target, n):
    answer = []

    index = 0
    for num in range(1, n+1):
        answer.append("Push")

        if num == target[index]:
            index += 1
        else:
            answer.append("Pop")

        if index == len(target):
            return answer

    return answer

t = [1,3]
n = 3
print(buildArray(t, n))