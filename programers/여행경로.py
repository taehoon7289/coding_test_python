def solution(tickets):
    answer = []

    def dfs(dests, visited, tickets):

        if len(tickets) == len([v for v in visited if v == 1]):
            answer.append(dests)
        else:
            for i in range(len(tickets)):
                start, end = tickets[i]
                if start == dests[-1] and visited[i] == 0:
                    c_visited = visited[:]
                    c_visited[i] = 1
                    dfs(dests + [end], c_visited, tickets)

    for i in range(len(tickets)):
        start, end = tickets[i]
        if start != 'ICN':
            continue
        visited = [0] * len(tickets)
        visited[i] = 1
        dfs([end], visited, tickets)
    if not answer:
        return []
    return ['ICN'] + sorted(answer)[0]


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
