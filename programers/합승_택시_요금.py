def solution(n, s, a, b, fares):
    # 총 n개 노드 1~n까지
    # s: 출발 노드
    # a, b : 도착 노드
    def bfs(start_n, end_n, graph):
        if start_n == end_n:
            return 0
        min_cost = float('inf')
        q = deque()
        visited = [0] * (n + 1)
        visited[start_n] = 1
        for next_n, cost in graph[start_n]:
            q.append([next_n, cost, visited])
        while q:
            now_n, now_cost, visited = q.popleft()
            if now_n == end_n:
                min_cost = min(min_cost, now_cost)
            else:
                for next_n, next_cost in graph[now_n]:
                    if visited[next_n] == 0:
                        c_visited = visited[:]
                        c_visited[next_n] = 1
                        q.append([next_n, now_cost + next_cost, c_visited])
        return min_cost

    # 합승했다가 또는 합승안하고 둘이 나눠서 타고 감.
    # 합승하고 같이 이동. 나눠서 이동
    graph = defaultdict(list)
    for f in fares:
        n1, n2, cost = f
        graph[n1].append([n2, cost])
        graph[n2].append([n1, cost])

    # 두사람이 어느 노드에서 만날때 노드 당 최소 cost
    # s 로 부터 각 노드의 최소 비용값구하기
    # 이 두개를 같은 노드 끼리 cost 더하면 됨.
    # answer = float('inf')
    answer = 0

    # for i in range(1, n + 1):
    #     a_cost, b_cost, s_cost = bfs(a, i, graph), bfs(b, i, graph), bfs(s, i, graph)
    #     print(a_cost, b_cost, s_cost)
    #     print(sum([a_cost, b_cost, s_cost]))
    #     answer = min(answer, sum([a_cost, b_cost, s_cost]))

    print(bfs(2, 1, graph))

    return answer


from collections import defaultdict, deque


def solution2(n, s, a, b, fares):
    # 총 n개 노드 1~n까지
    # s: 출발 노드
    # a, b : 도착 노드
    def get_parent(n, parent):
        if n == parent[n]:
            return n
        return get_parent(parent[n], parent)

    def union_parent(a, b, parent):
        a = get_parent(a, parent)
        b = get_parent(b, parent)
        # 최대한 부모노드가 적은숫자를 가진걸로 통일
        parent[max(a, b)] = min(a, b)

    def mst(n, fares):
        temp = sorted(fares, key=lambda s: s[2])
        parent = defaultdict(int)
        for i in range(1, n + 1):
            parent[i] = i
        result = []
        for fare in temp:
            n1, n2, cost = fare
            a, b = get_parent(n1, parent), get_parent(n2, parent)
            if a != b:
                result.append(fare)
                union_parent(a, b, parent)
            if len(result) == n - 1:
                break
        print(parent)
        return result

    def bfs(start_n, end_n, graph):
        if start_n == end_n:
            return 0
        min_cost = float('inf')
        q = deque()
        visited = [0] * (n + 1)
        visited[start_n] = 1
        for nn, cost in graph[start_n]:
            visited[nn] = 1
            q.append([nn, cost, visited])
        while q:
            now_n, now_cost, visited = q.popleft()
            if now_n == end_n:
                return now_cost
            else:
                for next_n, next_cost in graph[now_n]:
                    if visited[next_n] == 0:
                        visited[next_n] = 1
                        q.append([next_n, now_cost + next_cost, visited])
        return min_cost

    graph = defaultdict(list)
    # 두사람이 어느 노드에서 만날때 노드 당 최소 cost
    # s 로 부터 각 노드의 최소 비용값구하기
    # 이 두개를 같은 노드 끼리 cost 더하면 됨.
    # answer = float('inf')
    answer = n * 100000 + 1

    for n1, n2, cost in mst(n, fares):
        graph[n1].append([n2, cost])
        graph[n2].append([n1, cost])
    for i in range(1, n + 1):
        a_cost, b_cost, s_cost = bfs(a, i, graph), bfs(b, i, graph), bfs(s, i, graph)
        # print('------')
        # print(i)
        # print(a_cost, b_cost, s_cost)
        # print(sum([a_cost, b_cost, s_cost]))
        answer = min(answer, sum([a_cost, b_cost, s_cost]))

    return answer

from collections import defaultdict
import heapq
def solution3(n, s, a, b, fares):
    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
        res[start] = 0
        q = []
        # start 지점에서 거리 가까운거
        heapq.heappush(q, (res[start], start))
        while q:
            now_cost, now_n = heapq.heappop(q)
            for next_n, cost in graph[now_n]:
                if res[next_n] > now_cost + cost:
                    res[next_n] = min(res[next_n], now_cost + cost)
                    heapq.heappush(q, ([res[next_n], next_n]))
        return res

    answer = float('inf')
    graph = defaultdict(list)
    for n1, n2, cost in fares:
        graph[n1].append([n2, cost])
        graph[n2].append([n1, cost])

    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[a][i] + dist[b][i])
    return answer


# 밤늦게 귀가할 때 안전을 위해 항상 택시를 이용하던 무지는 최근 야근이 잦아져 택시를 더 많이 이용하게 되

if __name__ == '__main__':
    print(solution2(6, 4, 6, 2,
                    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                     [1, 6, 25]]))
    print(solution2(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution2(6, 4, 5, 6,
                    [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

    print(solution3(6, 4, 6, 2,
                    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                     [1, 6, 25]]))
    print(solution3(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution3(6, 4, 5, 6,
                    [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
