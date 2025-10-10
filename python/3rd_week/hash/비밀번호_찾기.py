n, m = input().split()

password_dict = {}

for _ in range(int(n)):
    site, password = input().split()
    password_dict[site] = password

for _ in range(int(m)):
    site = input()
    print(password_dict[site])
