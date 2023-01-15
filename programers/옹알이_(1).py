# 발음해야하는 단어
def solution(babbling):
    # 발음가능
    avail = ["aya", "ye", "woo", "ma"]
    answer = 0
    for w in babbling:
        start = 0
        end = 1
        for a in avail:
            while start < end and end <= len(w):
                if a == w[start:end]:
                    print(start, end, w[start:end], a)
                    answer += 1
                    break
                else:
                    end += 1
    return answer


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
