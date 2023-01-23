from itertools import product


def solution(word):
    answer = 0
    arr = []
    for i in range(1, 6):
        arr += list(map(lambda s: ''.join(s), list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))))
    arr.sort()
    answer = arr.index(word) + 1
    return answer


if __name__ == '__main__':
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
