from collections import defaultdict, deque


def solution(game_board, table):
    def rotate_board(board):
        w, h = len(board), len(board[0])
        arr = [[0] * w for _ in range(h)]
        for i in range(w):
            for j in range(h):
                arr[i][j] = board[j][w - i - 1]
        starter_r, starter_c = 0, 0
        starter_r_flag, starter_c_flag = False, False
        for i in range(w):
            if starter_r_flag:
                break
            for j in range(h):
                if arr[i][j] == 1:
                    starter_r = i
                    starter_r_flag = True
                    break
        for j in range(h):
            if starter_c_flag:
                break
            for i in range(w):
                if arr[i][j] == 1:
                    starter_c = j
                    starter_c_flag = True
                    break
        while starter_r > 0:
            arr.append(arr.pop(0))
            starter_r -= 1

        while starter_c > 0:
            for i in range(w):
                for j in range(h):
                    arr[i][j - 1], arr[i][j] = arr[i][j], 0
            starter_c -= 1
        return arr

    answer = 0
    box = defaultdict(list)
    block = defaultdict(list)
    box_key, block_key = 0, 0
    cases = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    max_row, max_col = len(game_board), len(game_board[0])
    for row in range(max_row):
        for col in range(max_col):
            if game_board[row][col] == 0:
                game_board[row][col] = 1
                queue1 = deque()
                queue1.append([row, col])
                box[box_key].append([row, col])
                while queue1:
                    now_r, now_c = queue1.popleft()
                    for p_r, p_c in cases:
                        next_r, next_c = now_r + p_r, now_c + p_c
                        if 0 <= next_r < max_row and 0 <= next_c < max_col:
                            if game_board[next_r][next_c] == 0:
                                game_board[next_r][next_c] = 1
                                box[box_key].append([next_r, next_c])
                                queue1.append([next_r, next_c])
                box_key += 1

            if table[row][col] == 1:
                table[row][col] = 0
                queue2 = deque()
                queue2.append([row, col])
                block[block_key].append([row, col])
                while queue2:
                    now_r, now_c = queue2.popleft()
                    for p_r, p_c in cases:
                        next_r, next_c = now_r + p_r, now_c + p_c
                        if 0 <= next_r < max_row and 0 <= next_c < max_col:
                            if table[next_r][next_c] == 1:
                                table[next_r][next_c] = 0
                                block[block_key].append([next_r, next_c])
                                queue2.append([next_r, next_c])
                block_key += 1

    box_boards = []
    for k, vs in box.items():
        rows = [v[0] for v in vs]
        cols = [v[1] for v in vs]
        min_r, min_c, max_r, max_c = min(rows), min(cols), max(rows), max(cols)
        max_v = max(max_r - min_r, max_c - min_c)
        box[k] = list(map(lambda b: [b[0] - min_r, b[1] - min_c], box[k]))
        box_board = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        for r, c in box[k]:
            box_board[r][c] = 1
        box_boards.append(box_board)

    block_boards = []
    for k, vs in block.items():
        rows = [v[0] for v in vs]
        cols = [v[1] for v in vs]
        min_r, min_c, max_r, max_c = min(rows), min(cols), max(rows), max(cols)
        max_v = max(max_r - min_r, max_c - min_c)
        block[k] = list(map(lambda b: [b[0] - min_r, b[1] - min_c], block[k]))
        block_board = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        for r, c in block[k]:
            block_board[r][c] = 1
        block_boards.append([block_board, 0])

    for box_board in box_boards:
        for block_board in block_boards:
            block, visited = block_board
            if visited == 0:
                case1 = block
                case2 = rotate_board(case1)
                case3 = rotate_board(case2)
                case4 = rotate_board(case3)
                if box_board == case1 or box_board == case2 or box_board == case3 or box_board == case4:
                    block_board[1] = 1
                    answer += sum(sum(block, []))
                    break

    return answer


if __name__ == '__main__':
    print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0]],
                   [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
