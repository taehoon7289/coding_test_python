def solution(cap, n, deliveries, pickups):
    answer = 0
    for i in range(n - 1, -1, -1):
        cnt = 0
        while deliveries[i] > 0 or pickups[i] > 0:
            deliveries[i] -= cap
            pickups[i] -= cap
            cnt += 1

        answer += (i + 1) * 2 * cnt
        if i > 0:
            deliveries[i - 1] += deliveries[i]
            pickups[i - 1] += pickups[i]

    return answer


if __name__ == '__main__':
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
