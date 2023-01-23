def solution(sizes):
    arr = list(map(lambda s: [s[0], s[1]] if s[0] > s[1] else [s[1], s[0]], sizes))
    w = max([a[0] for a in arr])
    h = max([a[1] for a in arr])
    answer = w * h
    return answer


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
