import heapq


def solution(book_time):
    book_time.sort(key=lambda x: x[0])

    answer = 0

    heap = []

    for book in book_time:
        start_hour, start_minute = map(int, book[0].split(":"))
        start_time = start_hour * 60 + start_minute

        end_hour, end_minute = map(int, book[1].split(":"))
        end_time = end_hour * 60 + end_minute + 10

        if len(heap) == 0:
            heapq.heappush(heap, end_time)
            answer += 1
            continue

        if heap[0] > start_time:
            heapq.heappush(heap, end_time)
            answer += 1
        elif heap[0] <= start_time:
            heapq.heappop(heap)
            heapq.heappush(heap, end_time)

    return answer


a = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(a))
