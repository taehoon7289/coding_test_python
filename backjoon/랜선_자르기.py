import sys


def solution():
    k, n = map(int, sys.stdin.readline().strip().split())
    arr = [int(sys.stdin.readline().strip()) for _ in range(k)]
    start, end = 1, max(arr)
    last_m = 1
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for a in arr:
            cnt += a // mid
        if cnt < n:
            end = mid - 1
        else:
            start = mid + 1
            last_m = mid
    return last_m


if __name__ == '__main__':
    print(solution())
