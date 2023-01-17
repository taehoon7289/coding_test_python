from collections import defaultdict, deque


def solution():
    n = int(input())
    p_cnt = int(input())
    paths = [list(map(int, input().split())) for _ in range(p_cnt)]
    obj = defaultdict(list)
    for path in paths:
        p_0, p_1 = path
        obj[p_0].append(p_1)
        obj[p_1].append(p_0)
    # print(n, p_cnt, paths, obj)
    bfs(n, obj)
    answer = 0
    visited = [0] * (n + 1)
    visited[1] = 1

    def dfs(index):
        nonlocal visited
        for next_node in obj[index]:
            if visited[next_node] < 1:
                visited[next_node] = 1
                nonlocal answer
                answer += 1
                dfs(next_node)

    dfs(1)
    print(answer)


def bfs(n, obj):
    answer = 0
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(1)
    visited[1] = 1
    while queue:
        node = queue.popleft()
        for next_node in obj[node]:
            if visited[next_node] < 1:
                visited[next_node] = 1
                answer += 1
                queue.append(next_node)
    print(answer)


if __name__ == '__main__':
    solution()
