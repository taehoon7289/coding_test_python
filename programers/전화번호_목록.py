def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        phone1 = phone_book[i-1]
        phone2 = phone_book[i]
        if phone2.startswith(phone1):
            return False
    return True

def solution2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))
    print(solution2(["119", "97674223", "1195524421"]))
    print(solution2(["123", "456", "789"]))
    print(solution2(["12", "123", "1235", "567", "88"]))
