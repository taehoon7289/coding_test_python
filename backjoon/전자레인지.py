def solution():
    n = int(input())
    arr = [300, 60, 10]
    result = [0, 0, 0]
    if n % 10 != 0:
        print(-1)
    else:
        i = 0
        while n > 1:
            if n < arr[i]:
                i += 1
                continue
            value = n // arr[i]
            n -= value * arr[i]
            result[i] += value
        print(*result)


if __name__ == '__main__':
    solution()
