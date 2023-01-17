from collections import deque


def solution():
    n = int(input())
    cases = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []
    for c in range(n):
        w, h, number = list(map(int, input().split()))
        points = [list(map(int, input().split())) for _ in range(number)]
        arr = [[0] * w for _ in range(h)]
        for x, y in points:
            arr[y][x] = 1
        queue = deque()
        answer = 0
        obj = {}

        for i_x in range(w):
            for i_y in range(h):

                while queue:
                    now_p = queue.popleft()
                    now_x, now_y = now_p
                    for case in cases:
                        c_x, c_y = case
                        n_x, n_y = now_x + c_x, now_y + c_y
                        if 0 <= n_x < w and 0 <= n_y < h:
                            if arr[n_y][n_x] == 1:
                                arr[n_y][n_x] = -1
                                queue.append((n_x, n_y))

                                obj[answer] += 1

                if arr[i_y][i_x] == 1:
                    arr[i_y][i_x] = -1
                    queue.append((i_x, i_y))
                    answer += 1
                    # print((i_x, i_y))
                    obj[answer] = 1
        results.append(answer)
    for res in results:
        print(res)


if __name__ == '__main__':
    solution()
