def solution(price, money, count):
    i = 1
    sum_value = 0
    while i <= count:
        # 이용시마다 누적 금액
        sum_value += (price * i)
        i += 1
    answer = max(sum_value - money, 0)
    return answer


if __name__ == '__main__':
    print(solution(3, 20, 4))
