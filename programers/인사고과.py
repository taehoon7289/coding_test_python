def solution(scores):
    wan = scores[0]
    sum_wan = sum(wan)
    scores = list(filter(lambda s: sum_wan <= sum(s), scores))
    n = len(scores)
    dp = [0] * n
    # 인센티브를 받지 못하는 사람 체크
    for i in range(n):
        p_1, p_2 = scores[i]
        for j in range(n):
            if i == j:
                continue
            n_1, n_2 = scores[j]
            if n_1 > p_1 and n_2 > p_2:
                dp[i] = -1
                break
            else:
                dp[i] = sum(scores[i])

    if dp[0] == -1:
        return -1

    temp = sorted(filter(lambda s: s > -1, dp), reverse=True)

    for i in range(len(temp)):
        if temp[i] <= sum_wan:
            return i + 1
    return i + 1


if __name__ == '__main__':
    print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
