def solution():
    n = int(input())
    arr = []
    i = 1
    while n != 0:
        while n > 0:
            n -= i
            arr.append(i)
            i += 1
        value = abs(n)
        if value in arr:
            arr.remove(value)
            n += value
    print(len(arr))


if __name__ == '__main__':
    solution()
