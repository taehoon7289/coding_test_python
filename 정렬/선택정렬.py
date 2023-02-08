def solution(arr):

    INF = float('inf')
    for i in range(len(arr)):
        min_info = [INF, i]
        for j in range(i, len(arr)):
            if min_info[0] > arr[j]:
                min_info = [arr[j], j]
        value, idx = min_info
        arr[i], arr[idx] = value, arr[i]
        print(arr)

    return arr


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(solution([3, 5, 8, 1, 4, 6, 7, 9, 2, 10]))
