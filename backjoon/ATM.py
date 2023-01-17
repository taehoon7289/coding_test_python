def solution():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    answer = 0
    acc = 0
    for i in range(n):
        acc += arr[i]
        answer += acc
    print(answer)


if __name__ == '__main__':
    solution()
