def dailyTemperature(temperatures):
    answer = [0] * len(temperatures)

    for i in range(0, len(temperatures) - 1):
        temperature = temperatures[i]
        days = 0
        for j in range(i + 1, len(temperatures)):
            days += 1
            if temperature < temperatures[j]:
                answer[i] = days
                break

    return answer

def solution(temperatures):
    n = len(temperatures)

    answer = [0] * n
    stack = [] # index

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer


t = [73,74,75,71,69,72,76,73]
#print(dailyTemperature(t))
print(solution(t))