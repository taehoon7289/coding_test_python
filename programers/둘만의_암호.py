def solution(s, skip, index):
    answer = ''
    for w in s:
        idx = ord(w)
        for _ in range(index):
            idx += 1
            if idx > 122:
                idx -= 26
            while chr(idx) in skip:
                idx += 1
                if idx > 122:
                    idx -= 26
        answer += chr(idx)
    return answer


from string import ascii_lowercase


def solution2(s, skip, index):
    answer = ''
    a_to_z = list(filter(lambda s: False if s in skip else True, ascii_lowercase))
    str_a_to_z = ''.join(a_to_z)
    for w in s:
        idx = str_a_to_z.find(w)
        value = idx + index
        if value > len(str_a_to_z) - 1:
            value -= len(str_a_to_z)
        answer += a_to_z[value]
    return answer


if __name__ == '__main__':
    # print(solution("aukks", "wbqd", 5))
    print(solution2("aukks", "wbqd", 5))
