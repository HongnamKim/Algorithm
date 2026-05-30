from collections import defaultdict

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    print(sorted_nums)

    count = defaultdict(int)

    for index, num in enumerate(sorted_nums):
        if count[num] != 0:
            continue
        count[num] = index

    print(count)
    answer = []
    for num in nums:
        answer.append(count[num])

    return answer


n = [8,1,2,2,3]
print(smallerNumbersThanCurrent(n))