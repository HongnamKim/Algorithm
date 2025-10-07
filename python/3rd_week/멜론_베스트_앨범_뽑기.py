from functools import cmp_to_key


def genre_cmp(a, b):
    if a[1] < b[1]:
        return 1
    else:
        return -1


def play_time_cmp(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] == b[1]:
        if a[2] < b[2]:
            return -1
        else:
            return 1
    else:
        return -1


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    play_times = []

    for i, genre in enumerate(genre_array):
        play_times.append([genre, play_array[i], i])

    play_times.sort(key=cmp_to_key(play_time_cmp))

    genre_total_play_time = {}
    for i, genre in enumerate(genre_array):
        play_time = genre_total_play_time.get(genre)
        if play_time:
            genre_total_play_time[genre] = play_time + play_array[i]
        else:
            genre_total_play_time[genre] = play_array[i]

    genres = []
    for genre in genre_total_play_time.keys():
        genres.append([genre, genre_total_play_time[genre]])

    genres.sort(key=cmp_to_key(genre_cmp))

    answer = []
    for genre in genres:
        aa = list(filter(lambda n: n[0] == genre[0], play_times))

        count = 0
        for a in aa:
            if count >= 2:
                break
            answer.append(a[2])
            count += 1

    return answer


print(
    "정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
    get_melon_best_album(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    ),
)
print(
    "정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
    get_melon_best_album(
        ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
        [2000, 500, 600, 150, 800, 2500, 2000],
    ),
)
