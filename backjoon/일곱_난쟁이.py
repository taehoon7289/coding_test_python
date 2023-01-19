from sys import stdin
def solution():
    arr = [int(stdin.readline()) for _ in range(9)]
    total_sum = sum(arr)
    break_flag = False
    for i in range(8):
        if break_flag:
            break
        for j in range(i+1, 9):
            if 100 == total_sum - (arr[i] + arr[j]):
                val1, val2 = arr[i], arr[j]
                arr.remove(val1)
                arr.remove(val2)
                break_flag = True
                break
    for i in sorted(arr):
        print(i)


if __name__ == '__main__':
    solution()