# 해시문제
def solution(nums):
    obj = {}
    for num in nums:
        if not num in obj:
            obj[num] = 1
        else:
            obj[num] += 1
    return min(len(obj.keys()), len(nums) // 2)


if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))
