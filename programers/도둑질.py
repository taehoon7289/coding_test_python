def solution(money):
    def check_index(length, i):
        if i >= length:
            return 0
        elif i - 1 < 0:
            return length - 1
        return i

    answer = 0
    length = len(money)
    _money = [[money[i], i] for i in range(length)]
    # _money.sort(key=lambda mm: (-mm[0], mm[1]))
    result = set()
    for v, i in _money:
        if not i in result:
            v, ii = max(_money[check_index(length, i)],
                        _money[check_index(length, i - 1)],
                        _money[check_index(length, i + 1)],
                        _money[check_index(length, i - 2)],
                        _money[check_index(length, i + 2)],
                        )

            if not ii in result:
                answer += v
                print('dd', v, ii)
                p_index, m_index = check_index(length, ii + 1), check_index(length, ii - 1)
                result.add(p_index)
                result.add(m_index)
                print('re', result)
    print(result)
    return answer


def solution2(money):
    answer = 0
    length = len(money)
    dp1 = [0 for _ in range(length)]
    dp2 = [0 for _ in range(length)]

    dp1[0] = money[0]
    dp1[1] = dp1[0]
    for i in range(2, length - 1):
        dp1[i] += max(dp1[i - 2] + money[i], dp1[i - 1])

    dp2[1] = money[1]
    for i in range(2, length):
        dp2[i] += max(dp2[i - 2] + money[i], dp2[i - 1])

    return max(max(dp1), max(dp2))

if __name__ == '__main__':
    # print(solution([1, 2, 3, 1]), 4)
    print(solution2([1, 2, 3, 1]), 4)
    # print(solution([1, 1, 4, 1, 4]), 8)
    print(solution2([1, 1, 4, 1, 4]), 8)
    # print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
    print(solution2([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
    # print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2001)
    print(solution2([1000, 1, 0, 1, 2, 1000, 0]), 2001)
    # print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
    print(solution2([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
    # print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    print(solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    # print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    print(solution2([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    # print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    print(solution2([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    # print(solution([1, 2, 3]), 3)
    print(solution2([1, 2, 3]), 3)
    # print(solution([91, 90, 5, 7, 5, 7]), 104)
    print(solution2([91, 90, 5, 7, 5, 7]), 104)
    # print(solution([90, 0, 0, 95, 1, 1]), 185)
    print(solution2([90, 0, 0, 95, 1, 1]), 185)
