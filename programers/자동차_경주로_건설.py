from collections import deque


def solution(board):
    INF = float('inf')
    answer = INF
    S, C = 100, 500
    max_row, max_col = len(board), len(board[0])
    visited = [[[INF] * 4 for _ in range(max_col)] for _ in range(max_row)]
    # visited = [[INF] * max_col for _ in range(max_row)]
    # 방향 유지하면서 이동 + 100
    # 방향 유지하면 + 0
    # 방향 바꾸면 + 500
    cases = [[1, 0], [-1, 0], [0, 1], [0, -1]]  #
    q = deque()
    # 현재col, 현재row, 방향index

    for i in range(len(cases)):
        visited[0][0][i] = 0
        q.append([0, 0, i])
    while q:
        # 도로 건설할 준비
        col, row, case = q.popleft()
        if col == max_col - 1 and row == max_row - 1:
            continue
        else:
            for i in range(len(cases)):
                u_case = (case + i) % 4
                next_col, next_row = col + cases[u_case][1], row + cases[u_case][0]
                if 0 <= next_row < max_row and 0 <= next_col < max_col:
                    if board[next_row][next_col] == 0:
                        plus = S + C if i > 0 else S
                        if visited[next_row][next_col][u_case] > visited[row][col][case] + plus:
                            visited[next_row][next_col][u_case] = visited[row][col][case] + plus
                            q.append([next_col, next_row, u_case])

    answer = visited[max_row - 1][max_col - 1]
    return min(answer)


if __name__ == '__main__':
    print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(solution(
        [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0]]))

    temp = [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0], ]
    print(solution(temp))
