def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling:
        for a in arr:
            if a in bab:
                bab = bab.replace(a, ' ')
        if bab.strip() == '':
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
