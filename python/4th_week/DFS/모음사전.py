def solution(word):
    char = ["A", "E", "I", "O", "U"]

    words = []
    path = []

    def dfs():
        len(path) and words.append("".join(path))

        if len(path) == 5:
            return

        for i in range(0, 5):
            path.append(char[i])
            dfs()
            path.pop()

    dfs()

    return words.index(word) + 1


a = "EIO"
print(solution(a))
