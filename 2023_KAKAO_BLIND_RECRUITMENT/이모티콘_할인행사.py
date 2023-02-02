from collections import defaultdict, deque
from itertools import product


def solution(users, emoticons):
    answer = []
    cases = [.1, .2, .3, .4]
    # 이모티콘별 각 할인율 계산후 가격
    emo_arr = [[0] * len(cases) for _ in range(len(emoticons))]
    for i in range(len(emoticons)):
        emo = emoticons[i]
        for j in range(len(cases)):
            c = cases[j]
            emo_arr[i][j] = emo * (1 - c)

    queue = deque()
    for n in range(len(users)):
        discount, max_amount = users[n]
        for j in range(len(cases)):
            if (discount / 10) - 1 <= j:
                # 구매함
                queue.append([n, 0, [j], emo_arr[0][j]])
            else:
                # 구매 안함
                queue.append([n, 0, [j], 0])
    cnt = 0
    obj = defaultdict(list)
    while queue:
        user_number, emo_number, select_discounts, amount = queue.popleft()
        discount, max_amount = users[user_number]
        if emo_number == len(emoticons) - 1:
            cnt += 1
            services_flag = False
            if amount >= max_amount:
                services_flag = True
            obj[tuple(select_discounts)].append([services_flag, amount, user_number])
        else:
            for j in range(len(cases)):
                if (discount / 10) - 1 <= j:
                    # 구매함
                    queue.append(
                        [user_number, emo_number + 1, select_discounts + [j], amount + emo_arr[emo_number + 1][j]])
                else:
                    # 구매 안함
                    queue.append([user_number, emo_number + 1, select_discounts + [j], amount])

    obj2 = defaultdict(lambda: [0, 0])
    for k, vs in obj.items():
        for flag, amount, us_number in vs:
            if not flag:
                obj2[k][1] += int(amount)
            else:
                obj2[k][0] += 1

    # [서비스 가입수, 이모티콘 매출액]
    return sorted(obj2.values(), reverse=True)[0]


if __name__ == '__main__':
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
                   [1300, 1500, 1600, 4900]))
    # # 이 가지수로 유저마다 서비스 가입, 아니면 구매가격 집계해서 최대서비스이면서 금액을 찾으면 됨.
    # temp = list(product([10, 20, 30, 40], repeat=4))
    # print(temp)
    # print(len(temp))
