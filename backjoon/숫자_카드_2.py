import bisect
import sys


def solution():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    arr.sort()
    m = int(sys.stdin.readline().strip())
    arr2 = list(map(int, sys.stdin.readline().strip().split()))
    answer = []
    for i in range(m):
        number = arr2[i]
        l_v = bisect.bisect_left(arr, number)
        r_v = bisect.bisect_right(arr, number)
        answer.append(str(r_v - l_v))

    return ' '.join(answer)


if __name__ == '__main__':
    print(solution())
