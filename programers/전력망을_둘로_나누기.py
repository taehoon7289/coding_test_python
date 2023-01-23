from collections import defaultdict, deque


def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        # 연결선 하나씩 빼고 반복
        graph = defaultdict(list)
        v_wires = wires[0:i] + wires[i + 1:]
        for j in range(len(v_wires)):
            n1, n2 = v_wires[j]
            graph[n1].append(n2)
            graph[n2].append(n1)

        arr_n = [0] * (n + 1)
        for ii in range(1, n + 1):
            visited = [ii]
            queue = deque()
            for next_n in graph[ii]:
                queue.append(next_n)
                visited.append(next_n)
            while queue:
                node = queue.popleft()
                next_ns = [n for n in graph[node] if not n in visited]
                if next_ns:
                    for next_nn in next_ns:
                        queue.append(next_nn)
                        visited.append(next_nn)
            arr_n[ii] = len(visited)
        result = arr_n[1:]
        answer = min(answer, max(result) - min(result))
    return answer


def solution2(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        # 연결선 하나씩 빼고 반복
        graph = defaultdict(list)
        v_wires = wires[0:i] + wires[i + 1:]
        for j in range(len(v_wires)):
            n1, n2 = v_wires[j]
            graph[n1].append(n2)
            graph[n2].append(n1)

        s1, s2 = wires[i]
        obj = {}
        for start_node in [s1, s2]:
            queue = deque()
            visited = [start_node]
            for next_n in graph[start_node]:
                queue.append(next_n)
                visited.append(next_n)
            while queue:
                node = queue.popleft()
                for n3 in [next_n2 for next_n2 in graph[node] if not next_n2 in visited]:
                    visited.append(n3)
                    queue.append(n3)
            obj[start_node] = len(visited)
        answer = min(answer, abs(obj[s1] - obj[s2]))
    return answer


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
    print(solution2(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution2(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution2(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
    print(solution2(3, [[1, 2], [2, 3]]))
