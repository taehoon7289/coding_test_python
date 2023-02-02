import sys


def solution():
    answer = ''
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    arr.sort()
    m = int(sys.stdin.readline())
    arr2 = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(m):
        search_num = arr2[i]
        start, end = 0, n-1
        search_flag = False
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == search_num:
                search_flag = True
                break
            if arr[mid] < search_num:
                start = mid + 1
            else:
                end = mid - 1
        if search_flag:
            answer += '1\n'
        else:
            answer += '0\n'
    return answer


if __name__ == '__main__':
    print(solution())
