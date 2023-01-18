from collections import deque


def solution():
    col, row = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]
    cases = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                queue.append((j, i, 0))

    max_d = 0
    while queue:
        x, y, d = queue.popleft()
        for case in cases:
            m_x, m_y = case
            n_x, n_y = m_x + x, m_y + y
            if 0 <= n_x < col and 0 <= n_y < row:
                if arr[n_y][n_x] == 0:
                    arr[n_y][n_x] = 1
                    queue.append((n_x, n_y, d + 1))
                    max_d = max(max_d, d + 1)
    exit_flag = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                exit_flag = True
                break
    if not exit_flag:
        print(max_d)
    else:
        print(-1)


if __name__ == '__main__':
    solution()
