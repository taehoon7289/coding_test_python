def solution(participant, completion):
    answer = ''
    obj = {}
    for p in participant:
        if not p in obj:
            obj[p] = 1
        else:
            obj[p] += 1
    for c in completion:
        obj[c] -= 1
    arr = sorted(obj.items(), key=lambda o: o[1], reverse=True)
    return arr[0][0]

# 괜찮은 풀이법
def solution2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

    print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution2(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))