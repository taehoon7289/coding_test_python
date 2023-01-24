def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l, r = 0, len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))
