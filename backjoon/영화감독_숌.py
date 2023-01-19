from sys import stdin


def solution():
    n = int(stdin.readline())
    i = 0
    value = 0
    while n > i:
        value += 1
        if '666' in str(value):
            i += 1
    print(value)


if __name__ == '__main__':
    solution()
