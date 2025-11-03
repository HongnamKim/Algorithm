def solution(cacheSize, cities):
    answer = 0

    cache = set()  # size == cacheSize
    order = []

    for city in cities:
        city = city.lower()

        print(order)

        if city in cache:
            answer += 1
            order.remove(city)
            order.append(city)

        else:
            cache.add(city)
            order.append(city)
            if len(order) > cacheSize:
                delete_city = order[0]
                order = order[1:]
                cache.remove(delete_city)
            answer += 5

    return answer


a = 3
b = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
]

aa = solution(a, b)

print()
print(aa)
