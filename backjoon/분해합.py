def solution():
    n = int(input())
    number = 1
    INF = float('inf')
    min_arr = [INF] * 2 * (n + 1)
    while number < n:
        value = number + sum(list(map(int, list(str(number)))))
        min_arr[value] = min(number, min_arr[value])
        number += 1
    if min_arr[n] == INF:
        print(0)
    else:
        print(min_arr[n])


if __name__ == '__main__':
    solution()
