def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    for r in reserve:
        arr[r - 1] += 1
    for l in lost:
        arr[l - 1] -= 1
    for i in range(len(arr)):
        if arr[i] == 0:
            if i > 0 and arr[i - 1] > 1:
                arr[i - 1] -= 1
                arr[i] += 1
            elif i < len(arr) - 1 and arr[i + 1] > 1:
                arr[i + 1] -= 1
                arr[i] += 1
    for i in range(len(arr)):
        if arr[i] > 0:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
