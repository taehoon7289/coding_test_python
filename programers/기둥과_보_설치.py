# "죠르디"는 기둥과 보

# 문제점1 :  row, col 에서 +1, -1 했을때 index error 를 쉽게 막는법 없을까? -> max, min 안됨!!! 조건에다가 row, col 체크 넣어주면 됨. 금방 넣음.
# 조건이 복잡한 문제일수록 우선 시간복잡도에 대해 계산해야된다.
# 조건이 복잡한거 일수록 조건 이해하고 그 조건만 반대 조건에도 적용시킨다. -> 여기서는 삭제하고 나서도 이 조건에 모두 적용되는지.


def solution(n, build_frame):
    # x ,y = col, row
    # a: 0 기둥, 1 보
    # b: 0 삭제, 1 설치
    # 보는 기둥이 있어야 설치 가능 -> 삭제 할때도 삭제후에 양옆의 보가 기둥이 있는지 체크 해야함.
    # 기본 col, row
    COL, BEAM = 0, 1
    answer = []

    # 기둥 설치, 삭제 가능여부 판단

    # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    def check_fun(col, row, a, coo, n):
        if a == 0:
            if row == 0:
                # 바닥이라면
                return True
            elif row > 0 and coo[row - 1][col][COL] == 1:
                # 아래에 기둥이 설치 되어있다면
                return True
            elif coo[row][col][BEAM] == 1:
                # 아래에 보가 설치 되어있다면
                return True
            elif col > 0 and coo[row][col - 1][BEAM] == 1:
                # 아래에 보가 설치 되어있다면
                return True
        elif a == 1:
            if row > 0 and col <= n and coo[row - 1][col][COL] == 1 or coo[row - 1][col + 1][COL] == 1:
                # 아래 기둥이 있다면 또는 오른쪽 아래 기둥이 있다면
                return True
            elif 0 < col <= n and coo[row][col - 1][BEAM] == 1 and coo[row][col + 1][BEAM] == 1:
                # 양옆으로 보가 설치 되있다면
                return True
        return False

    coo = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for bf in build_frame:
        col, row, a, b = bf
        if b == 0:
            # 없는데 삭제인경우 건너뛰기
            if not [col, row, a] in answer:
                continue
            else:
                answer.remove([col, row, a])
                coo[row][col][a] = 0
                for a_col, a_row, a_a in answer:
                    if not check_fun(a_col, a_row, a_a, coo, n):
                        # 삭제하면 조건에 안맞아서 다시 생성
                        answer.append([col, row, a])
                        coo[row][col][a] = 1
                        break

        elif b == 1:
            if [col, row, a] in answer:
                # 이미 포함
                continue
            elif check_fun(col, row, a, coo, n):
                coo[row][col][a] = 1
                answer.append([col, row, a])

    answer.sort()
    # 각 좌표에 설치된 구조물 리턴
    return answer


if __name__ == '__main__':
    print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                       [3, 2, 1, 1]]))
    print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                       [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
