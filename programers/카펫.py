def solution(b, y):
    m = ((2 + (b / 2)) + (4 + (2 * b) + ((b ** 2) / 4) - (4 * (y + b))) ** 0.5) // 2
    n = (b + y) / m
    return [int(m), int(n)]


if __name__ == '__main__':
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
