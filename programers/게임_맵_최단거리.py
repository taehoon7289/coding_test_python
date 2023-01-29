from collections import deque


def solution(maps):
    INF = float('inf')
    answer = INF
    max_row, max_col = len(maps), len(maps[0])
    queue = deque()
    cases = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    maps[0][0] = 1
    queue.append([1, 1, 1])
    while queue:
        now_r, now_c, cnt = queue.popleft()
        if now_r == max_row and now_c == max_col:
            answer = cnt
            break
        else:
            for p_r, p_c in cases:
                next_r, next_c = p_r + now_r, p_c + now_c
                if 0 < next_r <= max_row and 0 < next_c <= max_col and maps[next_r - 1][next_c - 1] == 1:
                    maps[next_r - 1][next_c - 1] += maps[now_r - 1][now_c - 1]
                    queue.append([next_r, next_c, cnt + 1])
    return -1 if answer == INF else answer


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
