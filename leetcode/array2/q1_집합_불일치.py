from collections import defaultdict, Counter

def findErrorNums(nums):

    #counter = defaultdict(int)
    counter = Counter(nums)
    print(counter)

    # for num in nums:
    #     counter[num] += 1

    a = 0
    b = 0
    for num in range(1, len(nums)+1):
        if counter[num] > 1:
            a = num
        elif counter[num] == 0:
            b = num

    return [a, b]


n = [1,2,2,4]
print(findErrorNums(n))