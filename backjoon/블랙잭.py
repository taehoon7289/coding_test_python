def solution():
    n, answer = map(int, input().split())
    arr = list(map(int, input().split()))
    INF = float('inf')
    min_value = INF
    min_diff = INF

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                value = sum([arr[i], arr[j], arr[k]])
                if value > answer:
                    continue
                elif value - answer == 0:
                    min_value = value
                    min_diff = answer - value
                    break
                diff = min(answer - value, min_diff)
                if min_diff > diff:
                    min_value = value
                    min_diff = diff
    print(min_value)


if __name__ == '__main__':
    solution()
