def solution(id_list, report, k):
    reports = {}
    emails = {}

    for id in id_list:
        reports[id] = 0
        emails[id] = 0

    report_logs = set(report)

    for r in report_logs:
        user, target = r.split(" ")
        reports[target] += 1

    banned_users = []
    for user, count in reports.items():
        if count >= k:
            banned_users.append(user)

    for report in report_logs:
        user, target = report.split(" ")
        if target in banned_users:
            emails[user] += 1

    print("reports: ", reports)
    print("banned_users: ", banned_users)
    print(emails)

    return list(emails.values())


a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
c = 2
# a = ["con", "ryan"]
# b = ["ryan con", "ryan con", "ryan con", "ryan con"]
# c = 3

print(solution(a, b, c))
