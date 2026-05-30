def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for n in nums:
        if n == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    return max(max_count, current_count)

n = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(n))