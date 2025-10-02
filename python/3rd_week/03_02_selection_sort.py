"""
배열에서 가장 작은 원소를 찾아서 앞으로 옮기기
1.
[4, 6, 2, 9, 1]
              -> 제일 작은 원소를 맨 앞으로
2.
[1, 6, 2, 9, 4]
        -> 2번째로
3.
[1, 2, 6, 9, 4]
             -> 3번째로
4.
[1, 2, 4, 9, 6]
             -> 4번째로
5.
[1, 2, 4, 6, 9] --> 정렬 완료

배열 길이 - 1 만큼 반복
옮기는 위치는 0, 1, 2, 3 ... 으로 반복 시행횟수
i 번째 요소를 검사할 때 0 ~ (i - 1) 번째 요소는 정렬이 된 상태임
"""

input = [4, 6, 2, 9, 1]

def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)): # i ~ 끝까지 가장 작은 원소 찾기
            if array[j] <= array[min_index]:
                min_index = j

        # 가장 작은 원소 앞으로 옮기기
        array[min_index], array[i] = array[i], array[min_index]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))