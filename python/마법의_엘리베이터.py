def solution(storey):

    count = 0
    while storey > 0:

        d = storey % 10
        storey = storey // 10

        # 4 이하일 경우 - 버튼
        if d < 5:
            count += d

        # 6 이상일 경우 + 버튼
        elif d > 5:
            count += 10 - d
            storey += 1  # 올림처리
        else:  # d == 5 일 경우
            if storey % 10 >= 5:
                storey += 1
                count += 10 - d
            else:
                count += d

    return count


a = 2554

aa = solution(a)
print()
print(aa)
