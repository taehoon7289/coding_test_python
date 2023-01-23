def solution(numbers):
    answer = ''
    str_numbers = list(sorted(map(map_number, numbers), reverse=True))
    answer = int(''.join(list(map(lambda s: s[1], str_numbers))))
    return str(answer)


def map_number(n):
    d = n % 10
    num = str(n)
    while len(num) < 4:
        num += num[0:4 - len(num)]
    return [int(num), str(n)]


if __name__ == '__main__':
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
