def solution():
    n = input()
    if not '0' in n:
        print(-1)
    else:
        arr = sorted(list(n), reverse=True)
        if sum(map(int, arr)) % 3 == 0:
            print(int(''.join(arr)))
        else:
            print(-1)




if __name__ == '__main__':
    solution()

