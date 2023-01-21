def solution(s):
    answer = True
    count = 0
    for i in range(len(s)):
        if count < 0:
            return False
        count += 1 if '(' == s[i] else -1
    return True if count == 0 else False


if __name__ == '__main__':
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution("(()("))
