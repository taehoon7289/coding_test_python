def solution(number, k):
    stack = []
    for n in number:
        if not stack:
            stack.append(n)
            continue

        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1

        stack.append(n)
    return ''.join(stack[0:len(stack) - k])


if __name__ == '__main__':
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
