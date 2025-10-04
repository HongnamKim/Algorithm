top_heights = [6, 9, 5, 7, 4]

def stack_answer(heights):
    stack = []
    answer = [0] * len(heights)

    for i in range(len(heights)):
        # stack 에 있는 탑이 현재 탑보다 낮으면, 그 다음 탑들은 현재 탑이 수신하므로 stack 에서 제거
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        # 현재 탑보다 높은 탑이 stack 에 존재
        if stack:
            answer[i] = stack[-1][0] + 1

        # 현재 탑을 stack 에 넣어서 다음 탑에서 확인할 수 있도록 함
        stack.append([i, heights[i]])

    return answer

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    for i in range(len(heights)-1, -1, -1):
        # i == 4 --> height[i] = 4

        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
print(' '.join(map(str, stack_answer(top_heights))))

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))