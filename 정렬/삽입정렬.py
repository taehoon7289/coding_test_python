def solution(arr):

    for i in range(1, len(arr)):
        while arr[i] < arr[i-1] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(solution([3, 5, 8, 1, 4, 6, 7, 9, 2, 10]))