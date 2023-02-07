def solution(triangle):
    answer = 0
    n = len(triangle)
    visited = [[0] * n for n in range(n, 0, -1)]
    for i in range(len(triangle[n - 1])):
        visited[0][i] = triangle[n - 1][i]
    for i in range(1, n):
        # i 는 층수
        for j in range(len(visited[i])):
            # j는 각 층수의 인덱스
            visited[i][j] = max(sum([visited[i - 1][j], triangle[n - i - 1][j]]),
                                sum([visited[i - 1][j + 1], triangle[n - i - 1][j]]))
    answer = visited[n - 1][0]
    return answer


def solution2(triangle):
    answer = 0
    n = len(triangle)
    visited = [[0] * n for n in range(1, n + 1)]
    for i in range(len(triangle[n - 1])):
        visited[n - 1][i] = triangle[n - 1][i]

    for i in range(n - 2, -1, -1):
        # i 는 층수
        for j in range(len(visited[i])):
            # j는 각 층수의 인덱스
            visited[i][j] = max(sum([visited[i + 1][j], triangle[i][j]]),
                                sum([visited[i + 1][j + 1], triangle[i][j]]))

    answer = visited[0][0]
    return answer



def solution3(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
    return triangle[0][0]

if __name__ == '__main__':
    # 처음에 생각한 역 삼각형 형태로
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    # 삼각형 형태에서 인덱스만 뒤에서 부터 시작
    print(solution2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    # 스킬체크로 나와서 다시 해봄
    print(solution3([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
