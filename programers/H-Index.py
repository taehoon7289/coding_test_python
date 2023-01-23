def solution(citations):
    answer = 0
    h = 0
    while True:
        arr = list(filter(lambda s: True if s >= h else False, citations))
        if len(arr) >= h:
            answer = h
            h += 1
        else:
            break
    return answer


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([2, 3, 6, 10, 20, 50]))
