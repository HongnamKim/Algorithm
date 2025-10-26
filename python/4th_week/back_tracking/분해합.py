import sys

input = sys.stdin.readline

n = int(input())

check = False
for m in range(1, n):
    part_sum = sum(map(int, str(m))) + m

    if part_sum == n:
        check = True
        print(m)
        break
if not check:
    print(0)
