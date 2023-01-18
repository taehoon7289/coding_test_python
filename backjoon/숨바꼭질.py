def solution(n, k):
    # n, k = list(map(int, input().split()))
    if n > k:
        # print(n - k)
        return n - k
    else:
        INF = float('inf')
        arr = [[i, INF] for i in range(2 * (k + 1) + 1)]
        index = n
        arr[index][1] = 0
        arr[index + 1][1] = min(arr[index][1] + 1, arr[index + 1][1])
        arr[index - 1][1] = min(arr[index][1] + 1, arr[index - 1][1])
        if index <= k:
            arr[index * 2][1] = min(arr[index][1] + 1, arr[index * 2][1])
        index += 1
        while index <= 2 * k:
            arr[index][1] = min(arr[index - 1][1] + 1, arr[index + 1][1] + 1)
            if index > 0 and index % 2 == 0:
                arr[index][1] = min(arr[index][1], arr[index // 2][1] + 1)
            arr[index + 1][1] = min(arr[index][1] + 1, arr[index + 1][1])
            arr[index - 1][1] = min(arr[index][1] + 1, arr[index - 1][1])
            if index <= k:
                arr[index * 2][1] = min(arr[index][1] + 1, arr[index * 2][1])
            print(arr)
            index += 1

        # print(arr[k][1])
        return arr[k][1]


from collections import deque


def solution2(n, k):
    # n, k = list(map(int, input().split()))
    if n > k:
        # print(n - k)
        return n - k
    else:
        arr = [[i, 0] for i in range(2 * (k + 1) + 1)]
        queue = deque()
        queue.append([n, 0])
        arr[n] = 1
        cases = [1, -1, 2]

        while queue:
            index, value = queue.popleft()
            if index == k:
                # print(value)
                return value
                break

            for case in cases:
                if case == 1:
                    n_index = index + 1
                elif case == -1:
                    n_index = index - 1
                else:
                    n_index = index * 2
                if 0 <= n_index <= 2 * (k + 1):
                    if arr[n_index] != 1:
                        arr[n_index] = 1
                        queue.append([n_index, value + 1])


import random

if __name__ == '__main__':
    print(solution(8, 47))
    print(solution2(8, 47))
    # while True:
    #     n = random.randrange(1, 100)
    #     k = random.randrange(1, 100)
    #     a = solution(n, k)
    #     b = solution2(n, k)
    #     if a != b:
    #         print(n , k, '다른거', a, b)
    #     # else:
    #     #     print(n , k, '같은거', a, b)
