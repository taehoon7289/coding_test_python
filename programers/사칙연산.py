def solution(arr):
    answer = -1
    min_v, max_v = 0, 0
    last_oper = '+'
    last_i = len(arr) - 1
    for i in range(len(arr) - 1, -1, -2):
        if i == 0:
            answer = max_v + int(arr[i])
            break
        oper, value = arr[i - 1:i + 1]
        if oper == '+':
            continue
        else:
            last_oper = '-'
            # 결합한 경우
            calc1 = eval(''.join(arr[i:last_i + 1]))
            # 결합 안한 경우 arr[i-1]에 음수값으로 해서 계산
            calc2 = eval(''.join(arr[i - 1:last_i + 1]))
            temp1 = [
                -(calc1 + max_v),
                calc2 + min_v,
            ]
            temp2 = [
                -(calc1 + min_v),
                calc2 + max_v,
            ]
            min_v, max_v = min(temp1), max(temp2)
            last_i = i - 2
    return answer


def solution2(arr):
    INF = float('inf')
    min_dp = [INF for _ in range(len(arr) // 2 + 1)]
    max_dp = [-INF for _ in range(len(arr) // 2 + 1)]
    # print(min_dp, max_dp)
    for i in range(len(arr) // 2 + 1):
        min_dp[i][i] = arr[i * 2 + 1]
        max_dp[i][i] = arr[i * 2 + 1]
    for c in range(1, len(max_dp)):
        for i in range(len(max_dp) - c):
            j = i + c
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                elif arr[k * 2 + 1] == "-":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
    return max_dp[0][-1]


def solution3(arr):
    minmax = [0, 0]
    sum_value = 0
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value + tempmin)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx + 1])
            minmax[1] = max(-(sum_value + tempmin), -minus_v + (sum_value - minus_v) + tempmax)
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
        # print('sum_value', sum_value)
    minmax[1] += sum_value
    return minmax[1]


def solution4(arr):
    print(-int('1'))
    i = 1
    while i < len(arr):
        if arr[i] == '+':
            arr = arr[0:i - 1] + [str(int(arr[i - 1]) + int(arr[i + 1]))] + arr[i + 2:]
        else:
            i += 2
    print(arr)
    min_max = [0, 0]
    for i in range(len(arr) - 2, -2, -2):
        # if i == 0:
        #     break
        n = int(arr[i + 1])
        min_max = [min(-(min_max[0] + n), min_max[0] - n),
                   max(n - min_max[1], min_max[1] - n)]
        print(n, i, min_max)


def solution5(arr):
    min_max = [0, 0]  # 이전 - 의 누적값
    sum_value = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            min_v, max_v = min_max
            # - 포함해서 계산, - 제외하고 계산하고 전체 -
            min_max[0] = min(-sum_value + min_v, -(sum_value + max_v))
            min_max[1] = max(sum_value - (2 * int(arr[i + 1])) + max_v, -(sum_value + min_v))
            sum_value = 0
        else:
            sum_value += int(arr[i])
    return sum_value


if __name__ == '__main__':
    # print(solution(["1", "-", "3", "+", "5", "-", "8"]))
    # print(solution2(["1", "-", "3", "+", "5", "-", "8"]))
    # print(solution3(["1", "-", "3", "+", "5", "-", "8"]))
    print(solution5(["1", "-", "3", "+", "5", "-", "8"]))
    # print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
    # print(solution2(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
    # print(solution3(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
    # temp = ["5", "-", "3", "-", "3", "-", "3", "-", "3", "-", "3", "+", "1", "+", "2", "-", "4"]
    # temp = ["5", "-", "3", "-", "3", "-", "3", "-", "3", "-", "6", "-", "4"]
    # print(solution(temp))  # 21
    # print(solution3(temp))
    # print(solution4(["1", "-", "3", "+", "5", "-", "8"]))
    # print(solution4(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
    # print(solution4(["5", "-", "3", "-", "3", "-", "3", "-", "3", "-", "3", "+", "1", "+", "2", "-", "4"]))
