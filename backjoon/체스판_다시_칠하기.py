from sys import stdin


def solution():
    row, col = map(int, stdin.readline().strip().split())
    arr = [list(stdin.readline().strip()) for _ in range(row)]
    result = [[[0,0]] * col for _ in range(row)]
    cases_0 = ['B', 'W']
    cases_1 = ['W', 'B']
    index = 0
    INF = float('inf')
    min_value = INF
    for n in range(row - 8, -1, -1):
        for m in range(col - 8, -1, -1):
            answer = [0, 0]
            for i in range(n, n + 8):
                for j in range(m, m + 8):
                    if arr[i][j] != cases_0[index % 2]:
                        answer[0] += 1
                    if arr[i][j] != cases_1[index % 2]:
                        answer[1] += 1
                    index += 1
                index += 1
            result[n][m] = answer
            min_value = min(*answer, min_value)
    print(min_value)




if __name__ == '__main__':
    solution()
