from collections import defaultdict

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(set(nums))

    count = defaultdict(int)

    for index, num in enumerate(sorted_nums):
        if count[num] != 0:
            continue
        count[num] = index

    answer = []
    for num in nums:
        answer.append(count[num])

    return answer


n = [7,7,7,7]
print(smallerNumbersThanCurrent(n))