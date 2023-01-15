def solution():
    n = int(input())
    ropes = [int(input()) for _ in range(n)]
    ropes.sort(reverse=True)
    max_v = ropes[0]
    for i in range(1, n):
        value = ropes[i] * (i + 1)
        if max_v < value:
            max_v = value
    print(max_v)


if __name__ == '__main__':
    solution()
