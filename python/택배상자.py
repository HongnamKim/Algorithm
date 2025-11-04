from collections import deque


def solution(orders):
    answer = 0
    n = len(orders)
    boxes = deque([i for i in range(1, n + 1)])
    queue = deque(orders)
    stack = []

    while boxes:
        if boxes[0] == queue[0]:
            # order 와 박스 번호 일치 --> 트럭에 옮기기
            answer += 1
            queue.popleft()
            boxes.popleft()
        else:
            # order 와 박스 번호 불일치
            # 1. 스택에서 꺼내올 수 있는지 --> 꺼낼 수 있다면 스택에서 트럭으로 옮기기
            if stack and stack[-1] == queue[0]:
                answer += 1
                stack.pop()
                queue.popleft()
            else:
                stack.append(boxes.popleft())

        print("stack ", stack)
        print("queue ", queue)

    print()
    while queue:
        print("stack ", stack)
        print("queue ", queue)
        if stack and stack[-1] == queue[0]:
            queue.popleft()
            stack.pop()
            answer += 1
        else:
            break

    return answer


a = [2, 1, 3, 4, 5]
aa = solution(a)

print()
print(aa)
