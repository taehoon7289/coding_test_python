def solution(operations):
    arr = []
    for oper in operations:
        o, number = oper.split()
        if o == 'I':
            arr.append(int(number))
        else:
            # D
            n = int(number)
            if arr:
                remove_n = n
                if n == 1:
                    remove_n = max(arr)
                elif n == -1:
                    remove_n = min(arr)
                arr.remove(remove_n)
    if not arr:
        return [0, 0]
    return [max(arr), min(arr)]


if __name__ == '__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
