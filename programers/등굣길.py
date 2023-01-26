from collections import deque


def solution(m, n, puddles):
    # m = col, n = row
    answer = 0
    INF = float('inf')
    visited = [[INF] * (m + 1) for _ in range(n + 1)]
    visited[1][1] = 0
    for p_row, p_col in puddles:
        visited[p_row][p_col] = -1
    cases = [[1, 0], [0, 1]]
    queue = deque()
    queue.append([1, 1, 0])  # row, col, cnt

    while queue:
        row, col, cnt = queue.popleft()
        # print(row, col, cnt)
        if row == n and col == m:
            answer += 1
            continue
        for n_r, n_c in cases:
            if 0 < n_r + row <= n and 0 < n_c + col <= m:
                if visited[n_r + row][n_c + col] > -1:
                    min_dist = min(visited[n_r + row][n_c + col], visited[row][col] + 1)
                    visited[n_r + row][n_c + col] = min_dist
                    queue.append([n_r + row, n_c + col, min_dist])
                
    print(visited)
    return answer


def solution2(m, n, puddles):
    # m = col, n = row
    answer = 0
    visited = [[0] * (m + 1) for _ in range(n + 1)]

    for p_col, p_row in puddles:
        visited[p_row][p_col] = -1
        if p_row == 1:
            for i in range(p_col, len(visited[p_row])):
                visited[p_row][i] = -1
        if p_col == 1:
            for i in range(p_row, len(visited)):
                visited[i][p_col] = -1
    for i in range(1, len(visited)):
        if visited[i][1] > -1:
            visited[i][1] = 1
    for i in range(1, len(visited[1])):
        if visited[1][i] > -1:
            visited[1][i] = 1
    visited[1][1] = 0
    for i in range(2, len(visited)):
        for j in range(2, len(visited[i])):
            if visited[i][j] == -1:
                continue

            p1 = 0 if visited[i - 1][j] < 0 else visited[i - 1][j]
            p2 = 0 if visited[i][j - 1] < 0 else visited[i][j - 1]
            visited[i][j] = (p1 + p2) % 1_000_000_007
    return visited[n][m] % 1_000_000_007


def solution3(m, n, puddles):
    visited = [[0] * (m + 1) for _ in range(n + 1)]

    for p_col, p_row in puddles:
        visited[p_row][p_col] = -1

    visited[1][1] = 1

    for i in range(1, len(visited)):
        for j in range(1, len(visited[i])):
            if i == j == 1:
                continue
            if visited[i][j] == -1:
                visited[i][j] = 0
                continue
            visited[i][j] = visited[i - 1][j] + visited[i][j - 1]
    print(visited)
    return visited[n][m] % 1_000_000_007


if __name__ == '__main__':
    # bfs로 풀었을때 시간초과 방법 <- 오류있음
    print(solution(4, 3, [[2, 2]]))
    print(solution(4, 3, [[2, 1], [2, 2]]))
    # [1,1] 0으로 시작하고 푼방법
    print(solution2(4, 3, [[2, 2]]))
    print(solution2(4, 3, [[2, 1], [2, 2]]))
    # [1,1] 1으로 시작하고 row : 0 , col : 0 인애들도 있어야 계산 가능한 방법 <- 가장 나은거같음
    print(solution3(4, 3, [[2, 2]]))
    print(solution3(4, 3, [[2, 1], [2, 2]]))
