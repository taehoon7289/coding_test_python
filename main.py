from collections import deque


def solution():
    # 시작노드, 갈수있는 노드 체크, 

    n_cnt, p_cnt, start = list(map(int, input().split()))
    paths = [list(map(int, input().split())) for _ in range(p_cnt)]
    visits = [False for _ in range(n_cnt + 1)]
    bfs_visit_order = [start]
    dfs_visit_order = [start]

    visits[start] = True
    bfs_queue, dfs_stack = deque(), []

    bfs_queue.append([bfs_visit_order])
    dfs_stack.append([dfs_visit_order])

    while bfs_queue:
        order = bfs_queue.popleft()
        for avail_path in avail_paths:
            next_index = avail_path[1]
            if next_index == now_index:
                next_index = avail_path[0]
            if now_visits[next_index]:
                continue
            visits[next_index] = True
            bfs_queue.append([next_index, now_visits])
    while dfs_stack:
        now_node = dfs_stack.pop()
        now_index, now_results, now_visits = now_node
        avail_paths = [path for path in paths if now_index in path]
        while avail_paths:
            for avail_path in avail_paths:
                next_index = avail_path[1]
                if next_index == now_index:
                    next_index = avail_path[0]
                if now_visits[next_index]:
                    continue
                now_index = next_index
                now_visits[next_index] = True
                now_results.append(next_index)
        print('dfs', now_results)

        # for i in range(1, len(visits) + 1):
        #     if not visits[i]:
        #         visits[i] = True
        #         results.append(i)


# def temp_lambda(arr):
#     print('arr', arr)
#     a = [i for i in range(int(arr[0]), int(arr[1]))]
#     print(a)
#     return a


if __name__ == '__main__':
    solution()
