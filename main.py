def solution():
    temp = [[i] * i for i in range(1, 10)]

    # j가 i 보다 1 작은 수까지 커지면서 반복한다.
    for i in range(len(temp)):
        for j in range(i):
            # print(i, j, i - 1 - j)
            for v1 in temp[j]:
                for v2 in temp[i - 1 - j]:
                    print(v1, v2)


if __name__ == '__main__':
    solution()
