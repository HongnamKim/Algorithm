def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t

    return m


def array_gcd(array):

    arr_gcd = array[0]
    for i in range(len(array) - 1):
        arr_gcd = gcd(arr_gcd, array[i + 1])

    return arr_gcd


def solution(arrayA, arrayB):

    gcd_a = array_gcd(arrayA)
    gcd_b = array_gcd(arrayB)

    print(gcd_a)
    print(gcd_b)

    for i in range(len(arrayB)):
        if arrayB[i] % gcd_a == 0:
            gcd_a = 0
            break
    for i in range(len(arrayA)):
        if arrayA[i] % gcd_b == 0:
            gcd_b = 0
            break

    return max(gcd_a, gcd_b)


a = [14, 35, 119]
b = [18, 30, 102]

result = solution(a, b)

print()
print(result)
