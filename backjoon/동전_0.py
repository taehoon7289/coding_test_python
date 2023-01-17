def solution():
    n, t = list(map(int, input().split()))
    coins = [int(input()) for _ in range(n)]
    i = n - 1
    answer = 0
    while t > 0 and i >= 0:
        if t >= coins[i]:
            v = t // coins[i]
            t -= v * coins[i]
            answer += v
        i -= 1
    print(answer)


if __name__ == '__main__':
    solution()
