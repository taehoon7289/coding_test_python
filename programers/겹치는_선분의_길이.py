def solution(lines):
    flat_lines = sum(lines, [])
    min_v = min(flat_lines)  # 0 부터 시작하도록
    max_v = max(flat_lines)
    temp = [[l[0] - min_v, l[1] - min_v] for l in lines]
    arr = [0] * (max_v - min_v + 1)
    for t in temp:
        start, end = t
        for i in range(start, end):
            arr[i] += 1
    answer = 0
    for a in arr:
        if a > 1:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution([[0, 2], [-3, -1], [-2, 1]]))
    print(solution([[0, 1], [2, 5], [3, 9]]))
    print(solution([[-1, 1], [1, 3], [3, 9]]))
    print(solution([[0, 5], [3, 9], [1, 10]]))
