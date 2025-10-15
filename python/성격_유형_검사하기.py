def solution(survey, choices):
    score = {
        "RT": [0, 0],  # {"R": 0, "T": 0},
        "CF": [0, 0],  # {"F": 0, "C": 0},
        "JM": [0, 0],  # {"M": 0, "J": 0},
        "AN": [0, 0],  # {"A": 0, "N": 0},
    }

    for i in range(len(survey)):
        if survey[i] == "RT":
            if choices[i] > 4:
                score["RT"][1] += abs(choices[i] - 4)
            elif choices[i] < 4:
                score["RT"][0] += abs(choices[i] - 4)
        elif survey[i] == "TR":
            if choices[i] < 4:
                score["RT"][1] += abs(choices[i] - 4)
            elif choices[i] > 4:
                score["RT"][0] += abs(choices[i] - 4)
        elif survey[i] == "FC":
            if choices[i] < 4:
                score["CF"][1] += abs(choices[i] - 4)
            elif choices[i] > 4:
                score["CF"][0] += abs(choices[i] - 4)
        elif survey[i] == "CF":
            if choices[i] < 4:
                score["CF"][0] += abs(choices[i] - 4)
            elif choices[i] > 4:
                score["CF"][1] += abs(choices[i] - 4)
        elif survey[i] == "MJ":
            if choices[i] > 4:
                score["JM"][0] += abs(choices[i] - 4)
            elif choices[i] < 4:
                score["JM"][1] += abs(choices[i] - 4)
        elif survey[i] == "JM":
            if choices[i] < 4:
                score["JM"][0] += abs(choices[i] - 4)
            elif choices[i] > 4:
                score["JM"][1] += abs(choices[i] - 4)
        elif survey[i] == "AN":
            if choices[i] > 4:
                score["AN"][1] += abs(choices[i] - 4)
            elif choices[i] < 4:
                score["AN"][0] += abs(choices[i] - 4)
        elif survey[i] == "NA":
            if choices[i] < 4:
                score["AN"][1] += abs(choices[i] - 4)
            elif choices[i] > 4:
                score["AN"][0] += abs(choices[i] - 4)

    # print(score)

    answer = ""

    for key, score in score.items():
        print(key, score)
        if score[0] > score[1]:
            answer += key[0]
        elif score[0] < score[1]:
            answer += key[1]
        else:
            answer += key[0]

    return answer


a = ["AN", "CF", "MJ", "RT", "NA"]
b = [5, 3, 2, 7, 5]

print(solution(a, b))
