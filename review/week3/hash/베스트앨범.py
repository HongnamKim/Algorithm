from collections import defaultdict

def solution(genres, plays):
    answer = []

    count = defaultdict(int)
    play_list = defaultdict(list)

    for i, items in enumerate(zip(genres, plays)):
        genre, play = items[0], items[1]
        play_list[genre].append((i, play))

    for genre, play in zip(genres, plays):
        count[genre] += play

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_count:
        l = sorted(play_list[genre], key=lambda x: x[1], reverse= True)
        c = 0
        for song in l:
            answer.append(song[0])
            c+=1
            if c == 2:
                break

    return answer

g = ["classic", "pop", "rock", "jazz", "classic", "pop", "rock", "jazz", "pop"]
p =  [500,       600,   400,   300,    800,       700,   200,   100,   900]
print(solution(g, p))

# 장르별 총 재생:
# - pop: 600 + 700 + 900 = 2200
# - classic: 500 + 800 = 1300
# - rock: 400 + 200 = 600
# - jazz: 300 + 100 = 400
#
# 기대값: [8, 5, 4, 0, 2, 6, 3, 7]