def count_down(number: int) -> None:
    print(number)
    if number < 0:
        return
    count_down(number - 1)

count_down(60)