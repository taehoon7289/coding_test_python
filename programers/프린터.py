from collections import deque


def solution(priorities, location):
    answer = 0
    arr = deque(list(map(list, zip(priorities, range(len(priorities))))))
    while arr:
        max_item = max(arr)
        value = arr.popleft()
        p_v, i_v = value
        if max_item[0] > p_v:
            arr.append(value)
        elif max_item[0] == p_v:
            answer += 1
            if i_v == location:
                break
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
