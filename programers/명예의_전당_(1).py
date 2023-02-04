def solution(k, score):
    answer = []
    arr = []
    for s in score:
        arr.append(s)
        arr.sort(reverse=True)
        answer.append(arr[min(k, len(arr)) - 1])
    return answer


if __name__ == '__main__':
    print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
    print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
