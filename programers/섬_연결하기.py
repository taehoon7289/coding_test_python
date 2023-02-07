def solution(n, costs):
    def find_parent(parent, n):
        if parent[n] == n:
            return parent[n]
        return find_parent(parent, parent[n])

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        # 최대한 부모노드가 적은숫자를 가진걸로 통일
        parent[max(a, b)] = min(a, b)

    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용 기준으로 오름차순 정렬
    parent = [i for i in range(n)]

    cnt = 0
    for node_a, node_b, cost in costs:
        if find_parent(parent, node_a) != find_parent(parent, node_b):
            union_parent(parent, node_a, node_b)
            answer += cost
            cnt += 1
        if cnt >= n - 1:
            break

    return answer


def solution2(n, costs):
    answer = 0

    def get_parent(n, parent):
        if n == parent[n]:
            return n
        return get_parent(parent[n], parent)

    costs.sort(key=lambda c: c[2])
    parent = [i for i in range(n)]

    for n1, n2, cost in costs:
        a, b = get_parent(n1, parent), get_parent(n2, parent)
        if a != b:
            parent[max(a, b)] = min(a, b)
            answer += cost
    return answer

if __name__ == '__main__':
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
    print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))

    print(solution2(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
    print(solution2(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
