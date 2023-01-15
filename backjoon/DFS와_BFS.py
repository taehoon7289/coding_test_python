from collections import defaultdict, deque


def solution():
    input_map = map(int, input().split())
    number, p, v = list(input_map)

    paths = [list(map(int, input().split())) for _ in range(p)]
    graph = defaultdict(list)
    for path in paths:
        graph[path[0]].append(path[1])
        graph[path[1]].append(path[0])
    queue = deque()
    queue.append(v)

    bfs_visited = [0] * (number + 1)
    bfs_visited[v] = 1
    bfs_result = [v]
    while queue:
        n = queue.popleft()
        for g in sorted(graph[n]):
            if bfs_visited[g] < 1:
                queue.append(g)
                bfs_visited[g] = 1
                bfs_result.append(g)

    dfs_visited = [0] * (number + 1)
    dfs_visited[v] = 1
    dfs_result = [v]

    dfs_visited, dfs_result = dfs(graph, v, dfs_visited, dfs_result)
    # print(dfs_result, bfs_result)
    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))


def dfs(graph, n, visited, result):
    visited[n] = 1
    result.append(n)
    for g in sorted(graph[n]):
        if visited[g] < 1:
            dfs(graph, g, visited, result)
    return visited, result


if __name__ == '__main__':
    print(solution())
