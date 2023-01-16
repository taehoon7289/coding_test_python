def solution(dots):
    cases = [((1, 2), (3, 4)), ((1, 3), (2, 4)), ((1, 4), (2, 3))]
    for c in cases:
        line1, line2 = c
        i1, i2 = line1
        x1, y1 = dots[i1 - 1]
        x2, y2 = dots[i2 - 1]
        m1 = (y2 - y1) / (x2 - x1)

        i3, i4 = line2
        x3, y3 = dots[i3 - 1]
        x4, y4 = dots[i4 - 1]
        m2 = (y4 - y3) / (x4 - x3)

        if m1 == m2:
            return 1
    return 0


if __name__ == '__main__':
    print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
    print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
