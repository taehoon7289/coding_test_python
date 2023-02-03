from collections import deque, defaultdict


def solution(n, t, m, timetable):
    timetable.sort()
    q = deque(timetable)
    start = "09:00"
    obj = defaultdict(list)
    for i in range(n):
        # 횟수별 탑승자 목록 뽑기
        if i > 0:
            hour, minutes = map(int, start.split(':'))
            minutes += t
            temp = [hour, minutes]
            if minutes >= 60:
                temp[0] = hour + minutes // 60
                temp[1] = minutes % 60
            start = str(temp[0]).zfill(2) + ':' + str(temp[1]).zfill(2)
        while q and len(obj[start]) < m:
            time = q[0]
            if start >= time:
                obj[start].append(q.popleft())
            else:
                break

    print(obj)
    # 뒤에서 부터 확인
    # 마지막 버스 자리가 비었다면 그 버스 출발시간에 오면됨.
    # 마지막 버스 자리가 없다면 버스 마지막 출발시간에서 맨 뒷사람보다 1분빨리오면 됨.
    last_time = sorted(obj.keys(), reverse=True)[0]
    if len(obj[last_time]) < m:
        return last_time
    else:
        if obj[last_time]:
            hour, minutes = map(int, sorted(obj[last_time], reverse=True)[0].split(':'))
            minutes -= 1
            if minutes < 0:
                hour -= 1
                minutes = 59
            answer = f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}'
        else:
            answer = last_time
    return answer


if __name__ == '__main__':
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
