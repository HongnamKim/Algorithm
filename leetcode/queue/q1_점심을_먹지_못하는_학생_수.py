from collections import deque


def countStudents(students, sandwiches):

    students = deque(students)
    sandwiches = deque(sandwiches)

    limit = len(students)
    count = 0
    while sandwiches:
        student = students.popleft()
        if sandwiches[0] == student:
            sandwiches.popleft()
            limit = len(students)
            count = 0
        else:
            students.append(student)
            count += 1
            if count == limit:
                break

    return len(students)

s = [1,1,1,0,0,1]
sw = [1,0,0,0,1,1]
print(countStudents(s, sw))
# print(solution(s, sw))