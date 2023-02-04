def solution(food):
    temp = ''
    for i in range(len(food)):
        temp += str(i) * (food[i] // 2)
    return temp + '0' + temp[::-1]


if __name__ == '__main__':
    print(solution([1, 3, 4, 6]))
    print(solution([1, 7, 1, 2]))
