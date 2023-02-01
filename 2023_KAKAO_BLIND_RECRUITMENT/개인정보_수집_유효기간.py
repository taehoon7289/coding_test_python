from collections import defaultdict


def solution(today, terms, privacies):
    answer = []

    def split_date(date):
        return map(int, date.split('.'))

    # 수집날짜로 부터 각 기간에 맞게 최대일 구하기
    def calc_date_add_month(date, add_month):
        year, month, day = split_date(date)
        while add_month > 0:
            month += 1
            add_month -= 1
            if month > 12:
                year += 1
                month = 1
        if day == 1:
            month -= 1
            if month == 0:
                year -= 1
                month = 12
            day = 28
        else:
            day = day - 1
        return year, month, day

    # 개인정보 종류별 기간
    term_obj = defaultdict(int)
    for term in terms:
        term, period_month = term.split()
        term_obj[term] = int(period_month)
    todays = list(split_date(today))
    for i in range(len(privacies)):
        pr = privacies[i]
        str_date, term = pr.split()
        year, month, day = calc_date_add_month(str_date, term_obj[term])
        if todays > [year, month, day]:
            answer.append(i + 1)

    # 파기해야할 번호 리스트 리턴 -> 오름차순으로 정렬
    return sorted(answer)


if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
                   ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    print(solution("2020.01.01", ["Z 3", "D 5"],
                   ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
