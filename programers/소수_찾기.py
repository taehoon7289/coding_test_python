from itertools import permutations


def solution(numbers):
    answer = 0
    arr = list(numbers)
    set_arr = set()
    for i in range(1, len(arr) + 1):
        arr_com = list(permutations(arr, i))
        for j in range(len(arr_com)):
            value = int(''.join(arr_com[j]))
            if prime_number_check(value):
                set_arr.add(value)
    answer = len(list(set_arr))
    return answer


def prime_number_check(n):
    if n <= 1:
        return False
    d = 2
    while d < n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True


if __name__ == '__main__':
    print(solution('17'))
    print(solution('011'))
