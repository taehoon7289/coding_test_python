def solution(food_times, k):
    answer = 0
    # 1~N 까지 음식
    total_seconds = sum(food_times)
    if total_seconds <= k:
        return -1
    # 음식 종류
    total_cnt = len(food_times)

    # 회전 가능
    while k // total_cnt > 0:
        rot = k // total_cnt
        remain_cnt = 0
        for i in range(total_cnt):
            if rot > food_times[i]:
                remain_cnt += (rot - food_times[i])
                food_times[i] = 0
            else:
                food_times[i] -= rot
        k -= (rot * total_cnt - remain_cnt)
    idx = 0

    while k > 0:
        if food_times[idx] > 0:
            food_times[idx] -= 1
            k -= 1
        idx += 1
        idx %= total_cnt
    while True:
        if food_times[idx] > 0:
            answer = idx + 1
            break
        idx += 1
        idx %= total_cnt

    # 주어진 k로 부터 몇번음식부터 먹으면 되는지 번호 리턴. 없으면 -1
    return answer


if __name__ == '__main__':
    print(solution([3, 1, 2], 5))
