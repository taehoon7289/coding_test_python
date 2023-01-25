def solution(routes):
    answer = 0
    routes.sort(key=lambda r: (r[1], r[0]))
    INF = float('inf')
    i = 0
    camera = -INF
    while i < len(routes):
        start, end = routes[i]
        if start > camera:
            answer += 1
            camera = end
        i += 1
    return answer


if __name__ == '__main__':
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
