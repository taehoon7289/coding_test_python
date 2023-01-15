def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    return arr.count(s)

if __name__ == '__main__':
    print(solution())