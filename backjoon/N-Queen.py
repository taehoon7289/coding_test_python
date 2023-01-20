import copy
from sys import stdin
import time


def solution():
    n = int(stdin.readline())
    chase = [[0] * n for _ in range(n)]
    answer = 0

    def block_box(chase, row, col):
        for i in range(len(chase)):
            if i != col:
                chase[row][i] = -1
        d = 1
        for j in range(row + 1, len(chase)):
            chase[j][col] = -1
            if col + d < len(chase):
                chase[j][col + d] = -1
            if col - d >= 0:
                chase[j][col - d] = -1
            d += 1
        return chase

    def dfs(case):
        chase, row, col = case
        chase[row][col] = 1
        if row >= len(chase) - 1:
            nonlocal answer
            answer += 1
            temp = []
            for i in range(len(chase)):
                for j in range(len(chase[i])):
                    if chase[i][j] == 1:
                        temp.append(j)
            print(temp)
            return
        chase = block_box(chase, row, col)
        for i in range(len(chase[row])):
            if chase[row + 1][i] == 0:
                dfs([[i[:] for i in chase], row + 1, i])

    for s in range(n):
        dfs([[i[:] for i in chase], 0, s])

    print(answer)


if __name__ == '__main__':
    start = time.time()
    solution()
    print(f'{time.time() - start}')
