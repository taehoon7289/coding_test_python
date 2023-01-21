def solution(prices):
    answer = list(range(len(prices) - 1, -1, -1))
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
