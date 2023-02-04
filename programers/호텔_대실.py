def solution(book_time):
    answer = 0

    def plus_time(time):
        h, m = map(int, time.split(':'))
        m += 10
        if m >= 60:
            h += 1
            m %= 60
        if h >= 24:
            h %= 24
        return str(h) + ':' + str(m)

    # 퇴실시간 기준으로 현재 사용중인방 max값을 체크
    book_time.sort(key=lambda s: s[1])
    book_time = list(map(lambda t: [t[0], plus_time(t[1])], book_time))
    print(book_time)
    for i in range(len(book_time)):
        s_t, e_t = book_time[i]
        cnt = 0
        for j in range(len(book_time)):
            s_t2, e_t2 = book_time[j]
            if s_t2 < e_t <= e_t2:
                cnt += 1
        answer = max(cnt, answer)
    # max 값 리턴
    return answer


def solution2(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)


if __name__ == '__main__':
    print(
        solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
    print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
    print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
