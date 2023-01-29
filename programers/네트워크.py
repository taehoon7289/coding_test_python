from collections import defaultdict


def solution(n, computers):
    def dfs(node, graph, visited):
        for i in list(graph[node]):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, graph, visited)

    answer = 0
    visited = [0] * n
    graph = defaultdict(set)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            dfs(i, graph, visited)

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(solution(7, [[1, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1]]))
