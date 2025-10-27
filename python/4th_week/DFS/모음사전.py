def solution(word):
    char = ["A", "E", "I", "O", "U"]

    words = []
    path = []

    def dfs(length):
        if len(path) == length:
            words.append("".join(path))
            return

        for i in range(0, 5):
            path.append(char[i])
            dfs(length)
            path.pop()

    for i in range(1, 6):
        dfs(i)

    words.sort()
    # print(words)
    #
    # test = []
    # for p in product(char, repeat=3):
    #     test.append("".join(p))
    # test.sort()
    # print(test)

    return words.index(word) + 1


a = "EIO"
print(solution(a))
