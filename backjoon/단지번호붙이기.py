from collections import deque


def solution():
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    cases = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    danji_cnt = 0
    obj = {}
    queue = deque()
    for i in range(n):
        for j in range(n):
            while queue:
                i1, j1 = queue.popleft()
                for case in cases:
                    m_r, m_c = case
                    n_r, n_c = i1 + m_r, j1 + m_c
                    if 0 <= n_r < n and 0 <= n_c < n:
                        if arr[n_r][n_c] > 0:
                            arr[n_r][n_c] = -1
                            queue.append((n_r, n_c))
                            obj[danji_cnt] += 1
            if arr[i][j] > 0:
                queue.append((i, j))
                arr[i][j] = -1
                danji_cnt += 1
                obj[danji_cnt] = 1
                continue
    print(danji_cnt)
    for i, v in sorted(list(obj.items()), key=lambda s: s[1]):
        print(v)


if __name__ == '__main__':
    solution()
