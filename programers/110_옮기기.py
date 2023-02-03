def solution(s):
    answer = []
    for num in s:
        cnt = 0
        while '110' in num:
            start = num.find('110')
            num = num[0:start] + num[start + 3:]
            cnt += 1
        for i in range(cnt):
            if not '0' in num:
                num = '110' + num
            else:
                index = len(num) - ''.join(reversed(num)).find('0')
                num = num[0:index] + '110' + num[index:]
        answer.append(num)
    return answer


if __name__ == '__main__':
    print(solution(["1110", "100111100", "0111111010"]))
