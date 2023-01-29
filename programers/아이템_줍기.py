from collections import deque


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


if __name__ == '__main__':
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
    print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
    print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
    print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
