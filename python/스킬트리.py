def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        required_skill = skill
        check = True
        for s in skill_tree:
            if s in required_skill:
                if s == required_skill[0]:
                    required_skill = required_skill[1:]
                else:
                    check = False
        if check:
            answer += 1

    return answer


a = "CBD"
b = ["BACDE", "CBADF", "AECB", "BDA"]

aa = solution(a, b)
print()
print(aa)
