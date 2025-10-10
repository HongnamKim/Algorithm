limit, student_count = map(int, input().split())

waiting_list = {}
aa = []

student_list = [
    "20103324",
    "20133221",
    "20133221",
    "20093778",
    "20140101",
    "01234567",
    "20093778",
    "20103325",
]

# for i in range(student_count):
for i, student in enumerate(student_list):
    # student = input()
    if student in waiting_list:
        index = waiting_list.get(student)
        aa[index] = ""
        waiting_list[student] = i
        aa.append(student)
    else:
        waiting_list[student] = i
        aa.append(student)

count = 0
for i in range(len(aa)):
    if aa[i] == "":
        continue
    print(aa[i])
    count += 1
    if count >= limit:
        break
