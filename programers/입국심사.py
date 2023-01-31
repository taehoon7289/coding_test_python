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


if __name__ == '__main__':
    print(solution(6, [7, 10]))
