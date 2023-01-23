from collections import deque


def solution(k, dungeons):
    answer = 0
    queue = deque()
    for i in range(len(dungeons)):
        need_k, minus_k = dungeons[i]
        visited = [0] * len(dungeons)
        if k >= need_k:
            visited[i] = 1
            queue.append([k - minus_k, visited])
    while queue:
        value = queue.popleft()
        cnt = 0
        for i in range(len(dungeons)):
            need_kk, minus_kk = dungeons[i]
            if value[1][i] == 0 and value[0] >= need_kk:
                cnt += 1
                now_k, now_visited = value
                temp = now_visited[:]
                temp[i] = 1
                queue.append([now_k - minus_kk, temp])
        if cnt < 1:
            now_k, now_visited = value
            temp2 = now_visited[:]
            answer = max(answer, temp2.count(1))
    return answer


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
