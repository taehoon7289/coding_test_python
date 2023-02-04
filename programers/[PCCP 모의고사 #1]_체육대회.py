from collections import deque


# 시간초과
def solution(ability):
    answer = 0
    q = deque()
    student_cnt = len(ability)
    type_cnt = len(ability[0])

    for i in range(student_cnt):
        q.append([[ability[i][0]], ability[0:i] + ability[i + 1:]])
    while q:
        jumsus, remain_students = q.popleft()
        if len(jumsus) >= type_cnt:
            answer = max(answer, sum(jumsus))
        else:
            for j in range(len(remain_students)):
                temp1 = jumsus + [remain_students[j][len(jumsus)]]
                temp2 = remain_students[0:j] + remain_students[j + 1:]
                q.append([temp1, temp2])
    return answer


from itertools import permutations



def solution2(ability):
    answer = 0
    student_cnt, play_cnt = len(ability), len(ability[0])
    for students in permutations(ability, play_cnt):
        jumsu = 0
        for j in range(play_cnt):
            jumsu += students[j][j]
        answer = max(answer, jumsu)
    return answer


if __name__ == '__main__':
    print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
    print(solution2([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
