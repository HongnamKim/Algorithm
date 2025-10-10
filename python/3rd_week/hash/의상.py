def solution(clothes):
    answer = 1

    codi = {}

    for cloth in clothes:
        category = cloth[1]
        codi.get(category)
        if codi.get(category):
            codi[category] += 1
        else:
            codi[category] = 1

    for a in codi.values():
        answer *= a + 1

    return answer - 1


clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))
