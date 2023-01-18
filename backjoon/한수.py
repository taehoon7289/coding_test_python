def solution():
    answer = 0
    n = int(input())
    number = 1
    while number <= n:
        arr = list(map(int, list(str(number))))
        if len(arr) < 3:
            answer += 1
        else:
            d = 0
            for i in range(1, len(arr)):
                if i == 1:
                    d = arr[i] - arr[i - 1]
                    continue
                if d != arr[i] - arr[i - 1]:
                    break
                if i == len(arr) - 1:
                    answer += 1
        number += 1

    print(answer)


if __name__ == '__main__':
    solution()
