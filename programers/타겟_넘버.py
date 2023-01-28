def solution(numbers, target):
    answer = 0

    def dfs(nums, idx, numbers, target):
        if idx == len(numbers):
            if target == sum(nums):
                nonlocal answer
                answer += 1
            return
        num = numbers[idx]
        dfs(nums + [num], idx + 1, numbers, target)
        dfs(nums + [-num], idx + 1, numbers, target)

    dfs([], 0, numbers, target)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
