def solution():
    answer = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        a_value, b_value = a[i], b[i]
        answer += (a_value * b_value)
    print(answer)
if __name__ == '__main__':
    solution()
