def shuffle(nums, n):
    answer = []
    for i in range(n):
        answer.append(nums[i])
        answer.append(nums[i + n])

    return answer


n = [2,5,1,3,4,7]
m = 3

print(shuffle(n, m))
