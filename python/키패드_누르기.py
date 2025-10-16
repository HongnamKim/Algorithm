def solution(numbers, hand):
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    num_position = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        11: (3, 0),
        0: (3, 1),
        12: (3, 2),
    }

    left_position = num_position[11]
    right_position = num_position[12]

    answer = ""

    for i, num in enumerate(numbers):
        if num in left_num:
            answer += "L"
            left_position = num_position[num]
        elif num in right_num:
            answer += "R"
            right_position = num_position[num]
        else:
            left_hand_distance = abs(left_position[0] - num_position[num][0]) + abs(
                left_position[1] - num_position[num][1]
            )
            right_hand_distance = abs(right_position[0] - num_position[num][0]) + abs(
                right_position[1] - num_position[num][1]
            )

            if left_hand_distance > right_hand_distance:
                answer += "R"
                right_position = num_position[num]
            elif left_hand_distance < right_hand_distance:
                answer += "L"
                left_position = num_position[num]
            else:
                if hand == "right":
                    answer += "R"
                    right_position = num_position[num]
                else:
                    answer += "L"
                    left_position = num_position[num]

        # print(left_position, right_position)

    return answer


n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = "right"

print(solution(n, h))
print("정답 여부: ", "LRLLLRLLRRL" == solution(n, h))
