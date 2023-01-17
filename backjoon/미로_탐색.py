from collections import deque


def solution():
    col, row = list(map(int, input().split()))
    arr = [list(input()) for _ in range(col)]
    arr.insert(0, ['0'] * row)
    for i in range(col + 1):
        arr[i].insert(0, '0')
        arr[i] = list(map(int, arr[i]))

    x, y = 1, 1
    cases = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque()
    queue.append((1, x, y))

    while queue:
        p = queue.popleft()
        length, p_x, p_y = p
        if p_x == col and p_y == row:
            print(length)
            break
        for case in cases:
            m_x, m_y = case
            next_x, next_y = p_x + m_x, p_y + m_y
            if 0 < next_x <= col and 0 < next_y <= row:
                if arr[next_x][next_y] > 0:
                    arr[next_x][next_y] = 0
                    queue.append((length + 1, next_x, next_y))


if __name__ == '__main__':
    solution()
