from collections import deque, defaultdict


def solution(maps):
    def bfs(row, col, graph, visited, obj, key):
        cases = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        q.append([row, col])
        visited[row][col] = 1
        obj[key] += graph[row][col]
        while q:
            r, c = q.popleft()
            for n_r, n_c in cases:
                m_r, m_c = r + n_r, c + n_c
                if 0 <= m_r < len(graph) and 0 <= m_c < len(graph[row]):
                    if graph[m_r][m_c] != 'X' and visited[m_r][m_c] == 0:
                        visited[m_r][m_c] = 1
                        q.append([m_r, m_c])
                        obj[key] += graph[m_r][m_c]

    answer = []
    row, col = len(maps), len(maps[0])
    graph = [[0] * col for _ in range(row)]
    for k in range(len(maps)):
        map = maps[k]
        arr = list(map)
        for i in range(len(arr)):
            v = arr[i]
            if v == 'X':
                graph[k][i] = 'X'
            else:
                graph[k][i] = int(v)
    visited = [[0] * col for _ in range(row)]
    key = 1
    obj = defaultdict(lambda: 0)
    for l in range(row):
        for m in range(col):
            if graph[l][m] != 'X' and visited[l][m] == 0:
                bfs(l, m, graph, visited, obj, key)
                key += 1
    if not obj:
        answer.append(-1)
    else:
        answer = list(obj.values())
        answer.sort()
    return answer


if __name__ == '__main__':
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
    print(solution(["XXX", "XXX", "XXX"]))
