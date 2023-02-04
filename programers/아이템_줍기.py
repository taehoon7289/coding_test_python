def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    p_set = set()
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x2 > x:
                    p_set.add((x + .5, y))
                if y2 > y:
                    p_set.add((x, y + .5))
                p_set.add((x, y))
    p_arr = list(p_set)
    filtered_arr = []
    for p_x, p_y in p_arr:
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            in_flag = True
            if x1 < p_x < x2 and y1 < p_y < y2:
                in_flag = False
                break
        if in_flag:
            filtered_arr.append([p_x, p_y])
    cases = [[.5, 0], [-.5, 0], [0, .5], [0, -.5]]
    queue = deque()
    visited = [0] * len(filtered_arr)
    for i in range(len(filtered_arr)):
        x, y = filtered_arr[i]
        if x == characterX and y == characterY and visited[i] == 0:
            visited[i] = 1
            queue.append([characterX, characterY, 0])
    while queue:
        now_x, now_y, cnt = queue.popleft()
        if now_x == itemX and now_y == itemY:
            answer = cnt // 2
            break
        for p_x, p_y in cases:
            next_x, next_y = now_x + p_x, now_y + p_y
            for i in range(len(filtered_arr)):
                x, y = filtered_arr[i]
                if x == next_x and y == next_y and visited[i] == 0:
                    visited[i] = 1
                    queue.append([next_x, next_y, cnt + 1])

    return answer


from collections import deque
from pprint import pprint


def solution2(rectangle, characterX, characterY, itemX, itemY):
    answer = float('inf')
    max_col, max_row = 0, 0
    rectangle = list(map(lambda s: [s[0] * 2, s[1] * 2, s[2] * 2, s[3] * 2], rectangle))
    for rec in rectangle:
        col1, row1, col2, row2 = rec
        max_col, max_row = max(max_col, col2 + 2), max(max_row, row2 + 2)
    arr = [[0] * (max_col) for _ in range(max_row)]

    for rec in rectangle:
        col1, row1, col2, row2 = rec
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                if row1 <= row <= row2:
                    if col == col1:
                        arr[row][col] = 1
                    elif col == col2:
                        arr[row][col] = 1
                if col1 <= col <= col2:
                    if row == row1:
                        arr[row][col] = 1
                    elif row == row2:
                        arr[row][col] = 1
    for rec in rectangle:
        col1, row1, col2, row2 = rec
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                if row1 < row < row2 and col1 < col < col2:
                    arr[row][col] = 0

    # pprint(arr)
    cases = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    q = deque()
    # col, row 순
    q.append([characterX * 2, characterY * 2, 0])
    while q:
        n_col, n_row, cnt = q.popleft()
        # print(n_col, n_row, cnt)
        if n_col == itemX * 2 and n_row == itemY * 2:
            answer = cnt
            break
        else:
            for next_r, next_c in cases:
                m_r, m_c = next_r + n_row, next_c + n_col
                if 0 <= m_r < max_row and 0 <= m_c < max_col:
                    if arr[m_r][m_c] == 1:
                        arr[m_r][m_c] += 1
                        q.append([m_c, m_r, cnt + 1])

    return answer // 2


if __name__ == '__main__':
    # print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    # print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
    # print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
    # print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
    # print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))

    print(solution2([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    print(solution2([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
    print(solution2([[1, 1, 5, 7]], 1, 1, 4, 7))
    print(solution2([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
    print(solution2([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
