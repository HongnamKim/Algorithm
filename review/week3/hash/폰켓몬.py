def solution(nums):
    answer = set(nums)
    return len(answer) if len(answer) < len(nums)//2 else len(nums)//2

n = [3,3,3,2,2,4]
print(solution(nums=n))