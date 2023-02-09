# 정수 N을 입력받아 N개의 데이터를 입력받는다. 이때, 데이터에서 인접한 값에는 접근을 할 수 없을 때, 데이터의 합산의 최대값을 구하자.
#
# ex) N = 4, [1, 3, 1, 5] -> 8
def solution1(n, arr):
    # 여기서 중요한 것은 당연히 점화식 -> 규칙을 찾는것
    # n = 1, sum[0]
    # n = 2, max(sum[0], arr[1])
    # n = 3, max(sum[1], sum[0] + arr[2])
    # 따라서 arr 한번 돌아서 각 인덱스까지의 최대 sum을 계산해 놔야하고, n 일때 최대 값을 확인해보면 됨.
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
    return max(dp[n - 1], dp[n - 2] + arr[i - 1])


# 정수 X를 입력받아, X를 네가지 연산을 조합하여 1로 만드는 최소회수를 구하자.
#
# 1) 5로 나누어 떨어지는 경우 5로 나눈다.
#
# 2) 3으로 나누어 떨어지는 경우 3으로 나눈다.
#
# 3) 2로 나누어 떨어지는 경우 2로 나눈다.
#
# 4) 1을 뺀다.
#
# ex) 26 : 25 -> 5 -> 1 (3번)
def solution2(x):
    dp = [0] * (x + 1)
    # 중요한점. 반대로 올라가는 걸로 생각!
    # 현재 인덱스에 들어간 값은 그 인덱스에 도달하기 위한 최소횟수이다.
    # 그럼 현재 숫자가 5로 나누어 떨어진다라고 하면 5로 나눈값 인덱스에서 + 1해준다.
    # 1 은 0임. 1은 애초에 1이니까 그래서 2부터 시작
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    return dp[x]


# 바닥의 세로 길이는 2로 고정되어 있다. 이때, 가로의 길이 N을 입력받아 세가지 형태의 타일로 덮을 수 있는 경우의 수를 구하자.
#
# 1) 가로 1, 세로 2
#
# 2) 가로 2, 세로 1
#
# 3) 가로 2, 세로 2
def solution3(w):
    # w = 1, dp[1] = 1
    # w = 2, dp[2] = 3
    # w = 3, dp[1] * 2 + dp[2] = 5
    dp = [0] * (w + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, w + 1):
        dp[i] = dp[i - 1] + (dp[i - 2] * 2)
    return dp[w]


if __name__ == '__main__':
    # print(solution1(4, [1, 3, 1, 5]))

    # print(solution2(x=26))
    # print(solution2(x=400))
    # print(solution2(x=1000))

    print(solution3(w=5))
