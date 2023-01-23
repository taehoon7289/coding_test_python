def solution(jobs):
    answer = 0
    t = 0
    done_jobs = []
    while len(done_jobs) < len(jobs):
        arr = [[t + jobs[i][1], *jobs[i], i] for i in range(len(jobs)) if jobs[i][0] <= t and not i in done_jobs]
        if arr:
            arr.sort()
            end_t, req_t, length_t, i = arr[0]
            answer += end_t - req_t
            t += length_t
            done_jobs.append(i)
        else:
            t += 1
    return answer // len(done_jobs)


import heapq


def solution2(jobs):
    answer, start_t, t = 0, -1, 0
    result, queue = [], []
    while len(result) < len(jobs):
        for arrive, length in jobs:
            if start_t < arrive <= t:
                heapq.heappush(queue, [length, arrive])
        if queue:
            task = heapq.heappop(queue)
            task_length, task_arrive = task
            start_t = t
            t += task_length
            answer += t - task_arrive
            result.append(task)
        else:
            t += 1
    return answer // len(result)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution2([[0, 3], [1, 9], [2, 6]]))
