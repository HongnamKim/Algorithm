def solution(sequence, k):
    answer = []
    left, right = 0, 0
    n = len(sequence)
    curr = sequence[0]
    while left < n and right < n:

        # 부분합이 k 보다 작을 때 right 증가
        if curr < k:
            right += 1
            if right == len(sequence):
                break
            curr = curr + sequence[right]
        elif curr > k:
            curr = curr - sequence[left]
            left += 1
            if left == len(sequence):
                break
        else:
            if not answer:
                answer = [left, right]
            else:
                if answer[1] - answer[0] > right - left:
                    answer[0] = left
                    answer[1] = right
            curr = curr - sequence[left]
            left += 1
            if left == len(sequence):
                break

    return answer


a = [1, 1, 1, 2, 3, 4, 5]
b = 5

aa = solution(a, b)
print()
print(aa)
