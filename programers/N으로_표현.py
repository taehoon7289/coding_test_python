def solution(N, number):
    answer = -1
    if N == number:
        return 1
    dp = [{int(str(N) * i)} for i in range(1, 9)]

    for i in range(len(dp)):
        for j in range(i):
            # i보다 작은 배열들의 한 배열의 인덱스의 양끝부분의 값들을 이중for문 돌면서 각각 사칙연산 값을 i 배열에 추가해준다.
            for v1 in dp[j]:
                for v2 in dp[i - j - 1]:
                    dp[i].update([v1 + v2, v1 - v2, v1 * v2])
                    if v2 != 0:
                        dp[i].add(v1 // v2)

    for i in range(len(dp)):
        if number in dp[i]:
            answer = i + 1
            break

    return answer


if __name__ == '__main__':
    print(solution(5, 12))
