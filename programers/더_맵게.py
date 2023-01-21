import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        val1 = heapq.heappop(scoville)
        if val1 >= K:
            break
        if len(scoville):
            val2 = heapq.heappop(scoville)
            heapq.heappush(scoville, val1 + (val2 * 2))
            answer += 1
        else:
            return -1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
