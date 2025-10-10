def solution(record):
    answer = []

    users = {}

    for log in record:
        a = log.split()

        if a[0] != "Leave":
            users[a[1]] = a[2]

        if a[0] == "Enter":
            answer.append(a[1] + "$$님이 들어왔습니다.")
        elif a[0] == "Leave":
            answer.append(a[1] + "$$님이 나갔습니다.")

    for i, log in enumerate(answer):
        uid, action = log.split("$$")
        nickname = users.get(uid)
        answer[i] = nickname + action

    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]

print(solution(record))
