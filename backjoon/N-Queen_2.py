import time
from sys import stdin


def solution():
    n = int(stdin.readline())
    answer = 0

    def dfs(cols, row):
        if row == n - 1:
            nonlocal answer
            answer += 1
            return
        for i in [j for j in range(n) if not j in cols]:
            avail_flag = True
            for row_i, col_i in enumerate(cols):
                if row + 1 - row_i == abs(i - col_i):
                    # 하나라도 대각선 있으면 안됌
                    avail_flag = False
                    break
            if avail_flag:
                dfs(cols + [i], row + 1)

    for s in range(n):
        dfs([s], 0)
    print(answer)


if __name__ == '__main__':
    start = time.time()
    solution()
    print(f'{time.time() - start}')
