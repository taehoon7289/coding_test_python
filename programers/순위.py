from collections import defaultdict


def solution(n, results):
    answer = 0
    graph_win, graph_lose = defaultdict(set), defaultdict(set)
    for res in results:
        w, l = res
        graph_win[w].add(l)  # 각 선수의 패배선수목록
        graph_lose[l].add(w)  # 각 선수의 이긴선수목록

    for i in range(1, n + 1):
        # i 선수가 패배한 선수 목록 -> winners
        for winner in graph_lose[i]:
            # i 가 이긴 선수 목록을 winner 목록에 추가
            graph_win[winner].update(graph_win[i])

        # i 선수가 이긴 선수 목록 -> losers
        for loser in graph_win[i]:
            # i 가 패배한 선수 목록을 loser 목록에 추가
            graph_lose[loser].update(graph_lose[i])
    for i in range(1, n + 1):
        # 목록을 합쳐서 n- 1개 있으면 확실히 등수 구분 가능
        if len(graph_lose[i]) + len(graph_win[i]) == n - 1:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
