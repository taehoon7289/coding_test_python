from collections import defaultdict, deque


def solution(n, edge):
    visited = [0] * (n + 1)
    graph = defaultdict(list)
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited[1] = 1
    queue = deque()
    queue.append([1, 1])
    while queue:
        n, cnt = queue.popleft()
        for node in graph[n]:
            if visited[node] == 0:
                visited[node] = cnt + 1
                queue.append([node, visited[node]])
    max_v = max(visited)
    return len([i for i in visited if i == max_v])


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
