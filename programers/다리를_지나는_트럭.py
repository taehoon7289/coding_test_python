from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_n = len(truck_weights)
    wait_queue = deque(map(list, zip(truck_weights, [0 for _ in range(len(truck_weights))])))
    bridge_queue = deque()
    done_queue = deque()
    while len(done_queue) != total_n:
        if bridge_queue:
            for i in range(len(bridge_queue)):
                bridge_queue[i][1] += 1
            if bridge_queue[0][1] == bridge_length:
                done_queue.append(bridge_queue.popleft())
        if wait_queue:
            if sum(w for w, t in bridge_queue) + wait_queue[0][0] <= weight:
                bridge_queue.append(wait_queue.popleft())
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
