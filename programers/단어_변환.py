def solution(begin, target, words):
    answer = float('inf')
    def dfs(begin, visited, words):
        nonlocal target
        if begin == target:
            nonlocal answer
            answer = min(answer, len([i for i in visited if i == 1]))
            return
        for i in range(len(words)):
            if visited[i] == 0:
                cnt = 0
                begin_list, word_list = list(begin), list(words[i])
                for b_i, w_i in zip(begin_list, word_list):
                    if b_i != w_i:
                        cnt += 1
                if cnt == 1:
                    c_visited = visited[:]
                    c_visited[i] = 1
                    dfs(''.join(word_list), c_visited, words)

    visited = [0] * len(words)
    if not target in words:
        return answer
    dfs(begin, visited, words)
    return answer


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
