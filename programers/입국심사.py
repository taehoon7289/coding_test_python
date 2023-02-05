def solution(n, times):
    times.sort()
    answer = times[-1] * n
    start, end = 0, answer
    while start <= end:

        mid = (end + start) // 2
        # 현재 중간 시간에서 최대로 심사받을수 있는 사람 수
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            answer = min(answer, mid)
        if n > count:
            # 적어도 가능한 값을 구하기 위해
            start = mid + 1
        else:
            # 최소값을 구하기위해
            end = mid - 1

    return answer

def solution2(n, times):
    # 걸리는 시간의 최소값
    answer = float('inf')
    # n명이 심사받는데 가장 오래걸리는 시간
    start, end = 0, max(times) * n
    while start <= end:
        # 걸리는 시간 가운데 값
        mid = (start + end) // 2
        # 이 시간동안 심사 받을수 있는 사람수 구하기
        cnt = 0
        for t in times:
            cnt += mid // t
        # cnt 값이 n 보다 작은 경우는 필요없고, 충족하는데 최소값을 찾을꺼라서
        if cnt >= n:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer

if __name__ == '__main__':
    print(solution(6, [7, 10]))
    print(solution2(6, [7, 10]))
