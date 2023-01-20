from collections import defaultdict


# 경우의 수를 어떻게 구하는지 중요
# 의상종류가 3개면 각각의 부위에서 안입는것,첫번째,두번째,세번째 총 4개의 선택이 가능하고 부위별로 가능한 선택 수를 곱하면 모든 조합이 나오는데 최소 하나는 입어야 해서 1을 빼야 합니다

def solution(clothes):
    answer = 1
    obj = defaultdict(int)
    for cloth in clothes:
        name, type = cloth
        obj[type] += 1
    for v in obj.values():
        answer *= v + 1
    return answer - 1


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
