def solution():
    n = int(input())
    n = 1000 - n
    charges = [500, 100, 50, 10, 5, 1]
    answer = 0

    while n > 0:
        for charge in charges:
            if n < charge:
                continue
            value = n // charge
            n -= value * charge
            answer += value
    print(answer)



if __name__ == '__main__':
    solution()