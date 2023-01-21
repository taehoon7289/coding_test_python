def solution(genres, plays):
    answer = []
    arr = list(zip(genres, plays))
    obj = {}
    for i in range(len(arr)):
        genre, play = arr[i]
        if not genre in obj:
            obj[genre] = {}
            obj[genre]['sum'] = play
            obj[genre]['ids'] = []
        else:
            obj[genre]['sum'] += play
        obj[genre]['ids'].append([play, i])
    arr2 = []
    for k, v in obj.items():
        t_sum, ids = obj[k]['sum'], obj[k]['ids']
        arr2.append([t_sum, k, ids])
    arr2.sort(reverse=True)
    for ii in arr2:
        ii[2].sort(key=lambda d: (-d[0], d[1]))
        min_len = min(len(ii[2]), 2)
        for iii in range(min_len):
            answer.append(ii[2].pop(0)[1])
    return answer


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
