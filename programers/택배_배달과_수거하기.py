def solution(cap, n, deliveries, pickups):
    answer = 0
    for i in range(n - 1, -1, -1):
        while deliveries[i] > 0 or pickups[i] > 0:
            deliveries[i] -= cap
            pickups[i] -= cap
            answer += (2 * (i + 1))
        if deliveries[i] < 0 and i > 0:
            deliveries[i - 1] += deliveries[i]
        if pickups[i] < 0 and i > 0:
            pickups[i - 1] += pickups[i]
    # print(deliveries, pickups)
    return answer


if __name__ == '__main__':
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
    print(solution(2, 2, [0, 0], [0, 4]))
    print(solution(2, 2, [0, 6], [0, 0]))
