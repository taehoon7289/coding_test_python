from collections import defaultdict


def solution(arrows):
    answer = 0
    cases = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1],
    ]
    visited, visited_dir = defaultdict(int), defaultdict(int)

    row, col = 0, 0
    visited[(row, col)] = 1
    for arrow in arrows:
        for _ in range(2):
            r, c = cases[arrow]

            if visited[(row + r, col + c)] == 0:
                visited[(row + r, col + c)] = 1
            else:
                if visited_dir[(row, col), (row + r, col + c)] == 0:
                    answer += 1
            visited_dir[(row, col), (row + r, col + c)] = 1
            visited_dir[(row + r, col + c), (row, col)] = 1
            row += r
            col += c
    return answer


if __name__ == '__main__':
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
