from collections import Counter

def solution(participant, completion):
    return (Counter(participant) - Counter(completion)).popitem()[1]
    # part = Counter(participant)
    #
    # for member in completion:
    #     part[member] -= 1
    #
    # answer = ''
    #
    # for member in part:
    #     if part[member] != 0:
    #         answer = member
    #
    # return answer

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

print(solution(p, c))