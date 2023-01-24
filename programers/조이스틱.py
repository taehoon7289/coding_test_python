from collections import deque


def solution(name):
    answer = 0
    visited = []
    start, end = ord('A'), ord('Z')
    cursor = 0

    for ii in range(1, len(name)):
        if name[ii] == 'A':
            visited.append(ii)

    queue = deque()
    visited.append(cursor)
    queue.append(cursor)
    answer += min(end - ord(name[cursor]) + 1, ord(name[cursor]) - start)

    while queue:
        now_cursor = queue.popleft()
        distances = [[min([abs(i - now_cursor), now_cursor + len(name) - i]), i] for i in range(len(name)) if
                     not i in visited]
        if distances:
            distances.sort(key=lambda ss: (ss[0], ss[1]))
            print(distances)
            min_dist = distances[0]

            dist, d_index = min_dist
            answer += dist
            answer += min(end - ord(name[d_index]) + 1, ord(name[d_index]) - start)
            # print('answer1', answer)
            visited.append(d_index)
            queue.append(d_index)

    return answer


def solution2(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # print(i , name, 'min_move', min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    # print('min_move', min_move)
    answer += min_move
    # print('answer2', answer)

    return answer


def solution3(name):
    answer = 0
    # 각 문자마다 상하 이동계산
    for i in range(len(name)):
        char = name[i]
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    min_move = len(name) - 1
    # 이제 이동만 계산함
    for i, v in enumerate(name):
        ii = i + 1
        while ii < len(name) and name[ii] == 'A':
            # 연속으로 'A' 가 있다면 어느 인덱스까지인지 확인 -> 'A'가 연속이라면 이 구간은 이동할 필요가 없으니까 -> 그래서 최대로 가장 많이 'A'가 연속인부분에서
            # 최소의 이동경로를 각각의 경우를 확인해서 최소값을 정한다.
            ii += 1
        min_move = min(min_move, 2 * i + len(name) - ii, 2 * (len(name) - ii) + i)
    print(min_move)
    answer += min_move

    return answer


if __name__ == '__main__':
    print(solution('JJJJAAAZ'))
    print(solution2('JJJJAAAZ'))
    print(solution3('JJJJAAAZ'))
    # print(solution('LABLPAJM'))
    # print(solution('BMOABA'))
    # print(solution('LAABAA'))
    # print(solution('AAAAAAAAJAAAA'))
    # print(solution('SAAAAAARRM'))
    # print(solution('RABAMATAWADLAFAVAAE'))
    # print(solution('XAAAAAABA'))
    # print(solution('AYOZAAVADAY'))
    # print(solution('AAFEASAAVA'))
    # print(solution('UAGAAASAAFAFXZA'))
    # print(solution('AAAAZAATAEA'))
    # print(solution('AACALATLAHABAA'))
    # print(solution('FAWJAAAFV'))
    # print(solution('AACAVAAPSAAOAA'))
    # print(solution('AKAAWAKX'))
    # print(solution('LOAAAHAJAAFAEBAWO'))
    # print(solution('AWAWVAQVAAA'))
    # print(solution('RCETAAAAVUEAETZAAAK'))
    # print(solution2('RCETAAAAVUEAETZAAAK'))
    # print(solution('BBBBAAAABA'))
    # print(solution2('BBBBAAAABA'))
    # print(solution('BBBAABB'))
    # print(solution2('BBBAABB'))
    # print(solution('AAAABABAAAA'))
    # print(solution2('AAAABABAAAA'))
    # print(solution('AAABBAAAAAAAAAAAAAAAABABAA'))
    # print(solution2('AAABBAAAAAAAAAAAAAAAABABAA'))
    # print(solution('AAABBBABA'))
    # print(solution2('AAABBBABA'))
    # print(solution('AAAAABBAAAAAAABAAA'))
    # print(solution2('AAAAABBAAAAAAABAAA'))
    # print(solution('GTAASKKAE'))
    # print(solution('AAAABAAAAAAKSAIQ'))
    # print(solution('ADASAAAUAAAPAA'))
    # print(solution('AAAAADBAAELSPUAAAOA'))
    # print(solution('VJAAIAFNAAAAA'))
    # print(solution('AARUAUAAHTBJAAYS'))
    # print(solution('IASAGITUPHE'))
    # print(solution('AAALAAAAAA'))
    # print(solution('AAAEASAHQAYTAAAJ'))
    # print(solution('BAALEAAAPMAAAHSRAV'))
    # print(solution('ASWAAATDAJAXA'))
    # print(solution('DYAOAAAARQANAWA'))
    # print(solution('AAIAPB'))

    # input: LABLPAJM / answer:61
    # input: BMOABA / answer:30
    # input: LAABAA / answer:15
    # input: AAAAAAAAJAAAA / answer:14
    # input: SAAAAAARRM / answer:41
    # input: RABAMATAWADLAFAVAAE / answer:78
    # input: XAAAAAABA / answer:6
    # input: AYOZAAVADAY / answer:35
    # input: AAFEASAAVA / answer:30
    # input: UAGAAASAAFAFXZA / answer:47
    # input: AAAAZAATAEA / answer:19
    # input: AACALATLAHABAA / answer:50
    # input: FAWJAAAFV / answer:35
    # input: AACAVAAPSAAOAA / answer:49
    # input: AKAAWAKX / answer:33
    # input: LOAAAHAJAAFAEBAWO / answer:79
    # input: AWAWVAQVAAA / answer:35
    # input: RCETAAAAVUEAETZAAAK / answer:75 //
    # input: GTAASKKAE / answer:52
    # input: AAAABAAAAAAKSAIQ / answer:49
    # input: ADASAAAUAAAPAA / answer:39
    # input: AAAAADBAAELSPUAAAOA / answer:70
    # input: VJAAIAFNAAAAA / answer:47
    # input: AARUAUAAHTBJAAYS / answer:69
    # input: IASAGITUPHE / answer:74
    # input: AAALAAAAAA / answer:14
    # input: AAAEASAHQAYTAAAJ / answer:60
    # input: BAALEAAAPMAAAHSRAV / answer:83
    # input: ASWAAATDAJAXA / answer:45
    # input: DYAOAAAARQANAWA / answer:66
    # input: AAIAPB / answer:24
