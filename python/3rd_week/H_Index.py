def solution(citations):
    citations.sort(reverse=True)
    print(citations)

    answer = 0
    for i in range(len(citations), 0, -1):
        count = 0
        for citation in citations:
            if citation >= i:
                count += 1
                if count >= i:
                    answer = max(answer, count)
                    break

    return answer

arr = [0] #[3, 0, 6, 1, 5]

print(solution(arr))

array = [3, 0, 6, 1, 5]
array.sort(reverse=True)
print(list(enumerate(array, start=1)))

