def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda s: (s[1], s[0]))
    answer = 0
    end = 0
    for i in range(n):
        if arr[i][0] >= end:
            answer += 1
            end = arr[i][1]
    print(answer)


if __name__ == '__main__':
    solution()