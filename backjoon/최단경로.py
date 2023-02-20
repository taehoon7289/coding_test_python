import heapq
import sys
from collections import defaultdict, deque


def solution():
    def dijkstra(start, v, graph):
        INF = float('inf')
        dist = [INF] * (v + 1)
        dist[start] = 0  # 자기 노드는 거리가 0
        q = []
        heapq.heappush(q, [dist[start], start]) # 거리가 짧은거부터 우선적으로 하기 위해 cost 값을 앞에다가 넣음.
        while q:
            now_cost, now_node = heapq.heappop(q)
            for next_cost, next_node in graph[now_node]:
                # 중요포인트
                if dist[next_node] > now_cost + next_cost:
                    # 최소값 등장시에만 우선순위큐에 넣기
                    dist[next_node] = now_cost + next_cost
                    heapq.heappush(q, [dist[next_node], next_node])
        return dist

    def dijkstra2(start, v, graph):
        INF = float('inf')
        dist = [INF] * (v + 1)
        dist[start] = 0  # 자기 노드는 거리가 0
        q = deque()
        q.append([dist[start], start])
        while q:
            now_cost, now_node = q.popleft()
            for next_cost, next_node in graph[now_node]:
                if dist[next_node] > now_cost + next_cost:
                    dist[next_node] = now_cost + next_cost
                    q.append([dist[next_node], next_node])
        return dist

    # 노드개수, 간선개수
    v, e = list(map(int, sys.stdin.readline().strip().split()))
    node = int(sys.stdin.readline().strip())
    paths = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(e)]
    graph = defaultdict(list)
    # 단방향인지 양방향인지
    for n1, n2, cost in paths:
        graph[n1].append([cost, n2])
        # graph[n2].append([cost, n1])

    # total_dist = [[]]
    # for i in range(1, v + 1):
    #     total_dist.append(dijkstra(i, v, graph))
    dist = dijkstra(node, v, graph)
    INF = float('inf')
    for j in range(1, len(dist)):
        if dist[j] == INF:
            print('INF')
        else:
            print(dist[j])

    dist = dijkstra2(node, v, graph)
    INF = float('inf')
    for j in range(1, len(dist)):
        if dist[j] == INF:
            print('INF')
        else:
            print(dist[j])

if __name__ == '__main__':
    solution()
