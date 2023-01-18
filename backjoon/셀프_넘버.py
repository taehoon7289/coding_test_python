def solution():
    arr = [0] * 10000
    n = 1
    while n < 10000:
        answer = 0
        answer += n + sum(map(int, list(str(n))))
        if answer < 10000:
            arr[answer] = 1
        n += 1
    for i, v in enumerate(arr[1:]):
        if v == 0:
            print(i + 1)


if __name__ == '__main__':
    solution()
