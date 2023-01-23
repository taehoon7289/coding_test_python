from collections import defaultdict


def solution(answers):
    answer = []
    arr_1, arr_2, arr_3 = [0] * len(answers), [0] * len(answers), [0] * len(answers)
    for i in range(len(arr_1)):
        arr_1[i] = (i % 5) + 1
    temp_2 = [1, 3, 4, 5]
    for i in range(len(arr_2)):
        if i % 2 == 0:
            arr_2[i] = 2
        else:
            arr_2[i] = temp_2[(i // 2) % 4]

    temp_3 = [3, 1, 2, 4, 5]
    for i in range(len(arr_3)):
        arr_3[i] = temp_3[(i // 2) % 5]

    obj = defaultdict(int)
    max_value = 0

    for i in range(len(answers)):
        if arr_1[i] == answers[i]:
            obj[1] += 1
        if arr_2[i] == answers[i]:
            obj[2] += 1
        if arr_3[i] == answers[i]:
            obj[3] += 1
    if obj:
        max_value = max(obj.values())

    for k, v in obj.items():
        if v == max_value:
            answer.append(k)

    return sorted(answer)


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
    print(solution([1, 3, 2, 4, 2, 2, 1, 3, 2, 1, 2, 1, 3, 1, 2, 2, 3, 5, 2, 1, 2, 3, 4, 5]))
    print(solution(
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 1]))
    print(solution(
        [4]))
