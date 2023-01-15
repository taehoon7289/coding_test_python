import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append([w, j])
        graph[j].append([w, i])
    # print(graph)
    INF = float('inf')
    visited = [INF] * (n + 1)
    summits.sort()
    summit_set = set(summits)
    queue = []
    for g in gates:
        heapq.heappush(queue, (0, g))
        visited[g] = 0

    while queue:
        print('queue', queue)
        intensity, node = heapq.heappop(queue)
        # 현재 intensity 보다 다른 케이스 에서 덮어쓴 intensity 보다 크면 할 필요 없음
        if node in summits:
            print(f'{node} 가 정상 이라 끝남')
            continue
        if intensity > visited[node]:
            print(f'{node} 버려짐')
            continue
        

        for w, next_node in graph[node]:
            # 갈만한 노드
            new_intensity = max(w, intensity)
            if new_intensity < visited[next_node]:
                print(f'{next_node}의 intensity 값이 덮어써짐', new_intensity)
                visited[next_node] = new_intensity
                heapq.heappush(queue, (new_intensity, next_node))

    print('visited', visited)

    result = [0, INF]
    for s in summits:
        if result[1] > visited[s]:
            result[0] = s
            result[1] = visited[s]
    return result


if __name__ == '__main__':
    # print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3],
    #                [5]))
    print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
