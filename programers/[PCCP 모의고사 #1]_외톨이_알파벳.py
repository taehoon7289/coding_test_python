from collections import defaultdict


def solution(input_string):
    answer = []
    obj = defaultdict(int)
    for s in input_string:
        if not s in obj:
            obj[s] = input_string.count(s)
    for s in obj.keys():
        word = s * obj[s]
        if not word in input_string:
            answer.append(s)
    if answer:
        answer.sort()
        return ''.join(answer)
    else:
        return 'N'


if __name__ == '__main__':
    print(solution("edeaaabbccd"))
    print(solution("eeddee"))
    print(solution("string"))
    print(solution("zbzbz"))
