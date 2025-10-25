def solution(s):
    nums = list(map(int, s.split()))

    min_num = min(nums)
    max_num = max(nums)

    return " ".join(map(str, [min_num, max_num]))


a = "1 2 3 4"
print(solution(a))
