def solution():
    line = input()
    temp = ''
    for s in line:
        if s == '+' or s == '-':
            temp += ' ' + s + ' '
        else:
            temp += s
    arr = temp.split()
    p_arr = [int(arr[0])]
    m_arr = []
    value = 0
    for i in range(1, len(arr), 2):
        if arr[i] == '-':
            value += 1
        if value > 0:
            m_arr.append(int(arr[i + 1]))
        else:
            p_arr.append(int(arr[i + 1]))
    print(sum(p_arr) - sum(m_arr))

if __name__ == '__main__':
    solution()