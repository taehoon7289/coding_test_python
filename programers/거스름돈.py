from collections import deque, defaultdict


# 시간 초과
def solution(n, money):
    queue = deque()
    queue.append([n, []])
    obj = defaultdict(int)
    while queue:
        now_n, arr = queue.popleft()
        if now_n == 0:
            obj[tuple(sorted(arr))] = 1
        else:
            for m in money:
                if now_n >= m:
                    queue.append([now_n - m, arr + [m]])
    answer = len(obj)
    # 1_000_000_007 로 나눈 값 리턴
    return answer % 1_000_000_007


# 동전 가지수가 이전 값에 의해서 누적이 되는지?
def solution2(n, money):
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(len(money)):
            if i == money[j]:
                visited[i] += 1
            elif i % money[j] == 0:
                visited[i] += 1
    print(visited)
    for i in range(1, n + 1):
        for m in money:
            if i >= m:
                if m > 1 and i - m > 1:
                    visited[i] = visited[i - m] + visited[m]
                    print('okok', i, m, visited)
    # print(visited)
    return visited[n] % 1_000_000_007


def solution3(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin, n + 1):
            print(price, coin, price - coin, dp[price - coin])
            # 각 동전으로 동전부터 시작해서 목표금액까지 만들수있는 가지수 더하기
            dp[price] += dp[price - coin]
            print(dp)
    # print(dp)
    return dp[n] % 1_000_000_007


def solution4(n, money):
    rest = [1] + [0] * n
    for m in money:
        for i in range(m, n + 1):
            if i >= m:
                rest[i] += rest[i - m]
    print(rest)
    return rest[n] % 1000000007


if __name__ == '__main__':
    # print(solution(5, [1, 2, 5]))
    # print(solution(8, [2, 8]))
    # print(solution2(5, [1, 2, 5]))
    # print(solution2(8, [2, 8]))

    print(solution3(5, [1, 2, 5]))
    print(solution3(8, [2, 8]))
    # print(solution4(5, [1, 2, 5]))
    # print(solution4(8, [2, 8]))
    # 1: 1원 1개
    # 2: 1원 2개, 2원 1개
    # 3: 1원 3개, 2원 1개 + 1원 2개
    # 4: 1원 4개, 2원 1개 + 1원 2개, 2원 두개
    # 5: 1원 5개, 2원 1개 + 1원 3개, 2원 2개 + 1원 1개, 5원 1개
