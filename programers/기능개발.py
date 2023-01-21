def solution(progresses, speeds):
    answer = []
    arr = list(map(list, zip(progresses, speeds)))
    while arr:
        for i in range(len(arr)):
            arr[i][0] += arr[i][1]
        cnt = 0
        while arr:
            if arr[0][0] >= 100:
                arr.pop(0)
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
