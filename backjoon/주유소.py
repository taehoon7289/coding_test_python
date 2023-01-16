# def solution():
#     n = int(input())
#     pays = list(map(int, input().split()))
#     nodes = list(map(int, input().split()))
#
#     i = n - 1
#     answer = 0
#     while i > 0:
#         min_index = i - 1
#         for j in range(i - 2, -1, -1):
#             if nodes[min_index] >= nodes[j]:
#                 min_index = j
#         answer += sum(pays[min_index:i]) * nodes[min_index]
#         i = min_index
#     print(answer)


def solution():
    n = int(input())
    pays = list(map(int, input().split()))
    nodes = list(map(int, input().split()))
    i_nodes = [0] * len(nodes)
    for i in range(len(nodes)):
        i_nodes[i] = (nodes[i], i)
    i_nodes.sort()

    i = n - 1
    c = 0
    answer = 0
    while i > 0:
        min_index = 0
        while True:
            cost, index = i_nodes[c]
            if i <= index:
                c += 1
                continue
            min_index = index
            break
        answer += sum(pays[min_index:i]) * nodes[min_index]
        i = min_index
    print(answer)


if __name__ == '__main__':
    solution()
