def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)

    counter = dict()

    answer = []

    for index, num in enumerate(sorted_nums):
        if num not in counter:
            counter[num] = index

    for num in nums:
        answer.append(counter[num])

    return answer


n = [8,1,2,2,3]
print(smallerNumbersThanCurrent(n))