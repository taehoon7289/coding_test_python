def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()
    while start <= end:
        # mid 는 최소값을 나타냄
        mid = (start + end) // 2
        remove_cnt = 0
        standard_start = 0
        min_dist = mid
        for i in range(len(rocks)):
            rock = rocks[i]
            if mid > rock - standard_start:
                remove_cnt += 1
            else:
                min_dist = min(min_dist, rock - standard_start)
                standard_start = rock
        if remove_cnt <= n:
            start = mid + 1
            answer = min_dist
        else:
            end = mid - 1
    return answer


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
