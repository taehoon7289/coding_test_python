from sys import stdin


def solution():
    n = int(stdin.readline())
    arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
    c_arr = arr.copy()
    result = [0] * n
    grade = 1
    while c_arr:
        max_w, min_h = sorted(c_arr, key=lambda a: (a[0], a[1]), reverse=True)[0]
        min_w, max_h = sorted(c_arr, key=lambda a: (a[1], a[0]), reverse=True)[0]
        # print(max_w, min_h, min_w, max_h)
        cnt = 0
        removes = []
        for i in range(len(arr)):
            if result[i] > 0:
                continue
            w, h = arr[i]
            if min_w <= w <= max_w and min_h <= h <= max_h:
                result[i] = grade
                cnt += 1
                removes.append(arr[i])
        grade += cnt
        for value in removes:
            c_arr.remove(value)
    print(*result)

def solution2():
    n = int(stdin.readline())
    arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
    result = [1] * n
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                result[i] += 1
    print(*result)



if __name__ == '__main__':
    solution2()
