def findDisappearedNumbers(nums):
    set_nums = set(nums)

    answer = []
    for i in range(1, len(nums) + 1):
        if i not in set_nums:
            answer.append(i)

    return answer

n = [1,1]
print(findDisappearedNumbers(n))