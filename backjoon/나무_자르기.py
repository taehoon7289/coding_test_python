import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    start, end = 0, max(arr)
    mid = (start + end) // 2
    last_v = mid
    while start <= end:
        # mid = 절단기 높이
        mid = (start + end) // 2
        sum_v = 0
        for a in arr:
            if a > mid:
                sum_v += a - mid
        if m > sum_v:
            end = mid - 1
        else:
            start = mid + 1
            last_v = mid
    return last_v


if __name__ == '__main__':
    print(solution())
