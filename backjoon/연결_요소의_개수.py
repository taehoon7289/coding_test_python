from collections import defaultdict, deque
from sys import stdin


def solution():
    n, l = list(map(int, stdin.readline().split()))
    lines = [list(map(int, stdin.readline().split())) for _ in range(l)]
    obj = defaultdict(list)
    for n1, n2 in lines:
        obj[n1].append(n2)
        obj[n2].append(n1)
    visited = [False] * (n + 1)
    queue = deque()
    answer = 0

    def bfs():
        while queue:
            node = queue.popleft()
            for n_node in obj[node]:
                if visited[n_node]:
                    continue
                visited[n_node] = True
                queue.append(n_node)

    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        queue.append(i)
        answer += 1
        bfs()
    print(answer)


if __name__ == '__main__':
    solution()
